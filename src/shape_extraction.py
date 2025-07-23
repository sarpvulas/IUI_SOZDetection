# src/shape_extraction.py

import numpy as np
import mne
from scipy.signal import hilbert


def extract_hfo_waveforms_in_segments(
    orig_data_list,
    downsampled_data_list,
    subject_run_list,
    segment_duration=1.0,
    l_freq=80.0,
    h_freq=120.0,
    threshold_factor=4.0,
    snippet_window=0.05,
):
    """
    Detect discrete HFO “events” (contiguous threshold crossings) on the downsampled data,
    then extract fixed-length raw-EEG snippets from the original (high-rate) data around each event’s true peak.

    Parameters
    ----------
    orig_data_list : list of mne.io.Raw
        List of pre-cropped EEG data at the ORIGINAL sampling rate (e.g. 2000 Hz).
    downsampled_data_list : list of mne.io.Raw
        List of the same EEG data after resampling to a LOWER sampling rate (e.g. 250 Hz).
        Must be in the same order as orig_data_list and subject_run_list.
    subject_run_list : list of (subject, run) tuples
        Pairs of subject ID and run ID, same order as orig_data_list (and downsampled_data_list).
    segment_duration : float
        Duration of each segment (seconds). Default is 1.0 s.
    l_freq, h_freq : float
        Lower and upper bounds for bandpass (Hz) to isolate HFO band. Defaults: 80–120 Hz.
    threshold_factor : float
        Number of standard deviations above mean envelope to mark a sample as “HFO candidate.”
    snippet_window : float
        Half-width of the snippet window around each event peak (seconds). Default 0.05 s
        → snippet length = 2 × snippet_window.

    Returns
    -------
    hfo_shape_results : dict
        {
          "sub-jh101_01": {
            "ChannelName": {
              seg_id: [  # list of events in this segment
                {
                  "start_ds": int,       # start index in downsamp domain
                  "end_ds": int,         # end index in downsamp domain
                  "peak_ds": int,        # index of envelope‐peak in downsamp domain
                  "peak_time": float,    # time (seconds) of the peak
                  "waveform": np.array(shape=(2*M+1,)),  # M = snippet_window * orig_sfreq
                },
                ...
              ],
              ...
            },
            ...
          },
          ...
        }
    """

    hfo_shape_results = {}

    # Loop over each run in parallel on original + downsampled data
    for idx, (orig_raw, ds_raw) in enumerate(zip(orig_data_list, downsampled_data_list)):
        subject, run = subject_run_list[idx]
        run_key = f"{subject}_{run}"
        hfo_shape_results[run_key] = {}

        # Sampling rates
        orig_sfreq = orig_raw.info["sfreq"]       # e.g. 2000 Hz
        ds_sfreq = ds_raw.info["sfreq"]           # e.g. 250 Hz

        # Compute how many samples per segment in downsampled domain
        ds_segment_samples = int(segment_duration * ds_sfreq)

        # Convert snippet_window (in seconds) to number of ORIGINAL‐rate samples
        orig_half_window = int(snippet_window * orig_sfreq)

        print(
            f"\n[extract_hfo_waveforms] Processing {run_key}: "
            f"orig_sfreq={orig_sfreq:.1f} Hz, ds_sfreq={ds_sfreq:.1f} Hz, "
            f"segment={segment_duration}s → {ds_segment_samples} ds‐samples/seg, "
            f"snippet_window={snippet_window}s → ±{orig_half_window} orig‐samples"
        )

        # Get .get_data() arrays for easier indexing
        #   orig_data[ch_idx] has length = total_orig_samples
        #   ds_data[ch_idx] has length  = total_ds_samples
        orig_data = orig_raw.get_data()   # shape (n_channels, total_orig_samples)
        ds_data = ds_raw.get_data()       # shape (n_channels, total_ds_samples)

        n_channels = len(orig_raw.ch_names)
        total_ds_samples = ds_data.shape[1]
        num_ds_segments = total_ds_samples // ds_segment_samples

        # For each channel:
        for ch_idx, ch_name in enumerate(orig_raw.ch_names):
            orig_ch_array = orig_data[ch_idx]
            ds_ch_array = ds_data[ch_idx]

            # Skip flat or NaN channels
            if np.all(orig_ch_array == 0) or np.any(np.isnan(orig_ch_array)):
                print(f"  Skipping {ch_name}: all‐zero or contains NaN")
                continue

            hfo_shape_results[run_key][ch_name] = {}

            # Process each segment in the downsampled domain
            for seg_id in range(num_ds_segments):
                ds_start = seg_id * ds_segment_samples
                ds_end = ds_start + ds_segment_samples
                segment_ds = ds_ch_array[ds_start:ds_end]  # length = ds_segment_samples

                # 1) Bandpass filter segment in HFO band (80–120 Hz) at ds_sfreq
                hfo_band_ds = mne.filter.filter_data(
                    segment_ds,
                    sfreq=ds_sfreq,
                    l_freq=l_freq,
                    h_freq=h_freq,
                    method="fir",
                    fir_design="firwin",
                )

                # 2) Compute Hilbert envelope at ds_sfreq
                envelope_ds = np.abs(hilbert(hfo_band_ds))
                env_mean = np.mean(envelope_ds)
                env_std = np.std(envelope_ds)
                threshold = env_mean + threshold_factor * env_std

                # 3) Find all sample indices (in downsampled domain) above threshold
                above_idx = np.where(envelope_ds > threshold)[0]
                if above_idx.size == 0:
                    # No HFO events in this segment
                    hfo_shape_results[run_key][ch_name][seg_id] = []
                    continue

                # 4) Group above_idx into contiguous runs (each run → one HFO event)
                events = []
                run_start = above_idx[0]
                prev = above_idx[0]
                for sample_idx in above_idx[1:]:
                    if sample_idx == prev + 1:
                        prev = sample_idx
                        continue
                    else:
                        # End of one run; record it
                        events.append((run_start, prev))
                        run_start = sample_idx
                        prev = sample_idx
                # Append the final run
                events.append((run_start, prev))

                segment_events = []

                # 5) For each discrete run, find the true envelope‐peak, then map to original
                for (e_start_ds, e_end_ds) in events:
                    # (a) Within this run, find the point of maximum envelope amplitude
                    local_env = envelope_ds[e_start_ds : e_end_ds + 1]
                    peak_offset = np.argmax(local_env)   # index relative to e_start_ds
                    peak_ds = e_start_ds + peak_offset   # absolute index in ds domain

                    # (b) Convert that downsampled‐index to time (seconds)
                    peak_time = peak_ds / ds_sfreq

                    # (c) Convert peak_time → original‐index in orig domain
                    orig_peak_idx = int(round(peak_time * orig_sfreq))

                    # (d) Compute snippet start/end in original samples
                    snippet_start_orig = orig_peak_idx - orig_half_window
                    snippet_end_orig = orig_peak_idx + orig_half_window + 1

                    # (e) Check boundaries in original data
                    total_orig_samples = orig_ch_array.shape[0]
                    if snippet_start_orig < 0 or snippet_end_orig > total_orig_samples:
                        # Too close to original edges → skip
                        continue

                    # (f) Extract raw‐EEG waveform from original data
                    waveform = orig_ch_array[snippet_start_orig : snippet_end_orig].copy()
                    # waveform.shape == (2*orig_half_window + 1,)

                    segment_events.append({
                        "start_ds": int(e_start_ds),
                        "end_ds": int(e_end_ds),
                        "peak_ds": int(peak_ds),
                        "peak_time": float(peak_time),
                        "waveform": waveform
                    })

                hfo_shape_results[run_key][ch_name][seg_id] = segment_events

    return hfo_shape_results
