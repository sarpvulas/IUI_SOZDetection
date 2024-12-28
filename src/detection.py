import numpy as np
import mne
from scipy.signal import hilbert

def detect_hfos_in_segments(
    cropped_data_list,
    subject_run_list,
    segment_duration=1,
    l_freq=80,
    h_freq=120,
    threshold_factor=4
):
    """
    Detect HFOs (ripples) by bandpass filtering and thresholding the Hilbert envelope.

    Parameters
    ----------
    cropped_data_list : list of mne.io.Raw
        List of cropped EEG data.
    subject_run_list : list of (subject, run)
        Subject/run pairs corresponding to each entry in cropped_data_list.
    segment_duration : float
        Duration of each segment in seconds.
    l_freq : float
        Lower bound for HFO band.
    h_freq : float
        Upper bound for HFO band.
    threshold_factor : float
        # of std devs above mean envelope to count as an HFO event.

    Returns
    -------
    hfo_results : dict
        { "sub-jh101_01": { "ChannelName": [counts_per_segment], ...}, ... }
    """
    hfo_results = {}

    for idx, cropped_data in enumerate(cropped_data_list):
        subject, run = subject_run_list[idx]
        run_key = f"{subject}_{run}"
        hfo_results[run_key] = {}

        sfreq = cropped_data.info['sfreq']
        segment_samples = int(segment_duration * sfreq)

        print(f"\nProcessing {run_key}: sfreq={sfreq} Hz, segment={segment_duration} s -> {segment_samples} samples/seg")

        for ch_idx, ch_name in enumerate(cropped_data.ch_names):
            channel_data = cropped_data.get_data(picks=ch_idx)[0]
            if np.all(channel_data == 0) or np.any(np.isnan(channel_data)):
                print(f"Skipping {ch_name}: data is all-zero or NaN.")
                continue

            total_samples = len(channel_data)
            num_segments = total_samples // segment_samples
            hfo_results[run_key][ch_name] = []

            for seg_id in range(num_segments):
                start_idx = seg_id * segment_samples
                end_idx = start_idx + segment_samples
                segment_data = channel_data[start_idx:end_idx]

                # Filter in HFO band
                hfo_band_data = mne.filter.filter_data(
                    segment_data,
                    sfreq=sfreq,
                    l_freq=l_freq,
                    h_freq=h_freq,
                    method='fir',
                    fir_design='firwin'
                )
                # Envelope
                envelope = np.abs(hilbert(hfo_band_data))
                threshold = np.mean(envelope) + threshold_factor * np.std(envelope)

                hfo_events = np.where(envelope > threshold)[0]
                hfo_count = len(hfo_events)
                hfo_results[run_key][ch_name].append(hfo_count)

    return hfo_results


def group_channels_by_soz(run_key, surgery_outcome_dict):
    """
    Given a run_key like 'sub-jh101_01', fetch channels from surgery_outcome_dict
    and separate them into SOZ vs. non-SOZ.

    Parameters
    ----------
    run_key : str
        e.g. 'sub-jh101_01'
    surgery_outcome_dict : dict
        { (sub, run): { 'channels': [...], 'soz_channels': [...], ...}, ... }

    Returns
    -------
    (soz_channels, non_soz_channels) : (list, list)
    """
    subject, run_num = run_key.split('_', 1)
    # Ensure run is 2-digit if needed
    doc_info = surgery_outcome_dict.get((subject, run_num.zfill(2)), {})

    if not doc_info:
        print(f"No matching info in surgery_outcome_dict for {run_key}.")
        return [], []

    all_channels = doc_info.get('channels', [])
    soz_channels = doc_info.get('soz_channels', [])
    non_soz_channels = [ch for ch in all_channels if ch not in soz_channels]
    return soz_channels, non_soz_channels
