import time
import warnings
import pandas as pd
import numpy as np
import mne
from mne_bids import BIDSPath

warnings.filterwarnings("ignore", category=RuntimeWarning)


def read_data(base_path, subjects_dict, subject_keywords, sample_rates):
    """
    Reads EEG data from BrainVision .vhdr files, drops bad channels, and crops
    around seizure onset times specified by events TSV files.

    Parameters
    ----------
    base_path : str
        Path to the EEG_Dataset folder (BIDS-like structure).
    subjects_dict : dict
        Dictionary mapping each subject to a list of runs.
    subject_keywords : dict
        Dictionary containing seizure onset keywords for each subject/run.
    sample_rates : dict
        Dictionary containing sampling rates for each subject/run.

    Returns
    -------
    all_raw_data : list of mne.io.Raw
        List of cropped MNE Raw objects.
    seizure_windows : dict
        Dictionary of start/end sample windows keyed by 'subject_run_onset_sample'.
    """
    counter = 0
    all_raw_data = []
    seizure_windows = {}

    for subject, runs in subjects_dict.items():
        for run in runs:
            counter += 1

            bids_data_path = BIDSPath(
                root=base_path,
                subject=subject.replace("sub-", ""),
                session='presurgery',
                task='ictal',
                acquisition="ecog",
                run=run,
                suffix='ieeg',
                extension='.vhdr'
            )
            # Typically: <base_path>/<subject>/presurgery/ieeg/<file>.vhdr
            # But might differ in your structure, so adjust as needed
            bids_data_path = bids_data_path.directory / "ieeg" / bids_data_path.basename

            print(f"Subject: {subject}, run: {run}, recording #: {counter}")

            # Read BrainVision file
            try:
                raw_data = mne.io.read_raw_brainvision(str(bids_data_path), preload=True)
            except FileNotFoundError:
                print(f"File not found for Subject {subject}, Run {run}")
                continue

            # Drop bad channels
            channels_tsv_path = (
                bids_data_path.with_suffix('.tsv').as_posix().replace('_ieeg', '_channels')
            )
            try:
                channels_data = pd.read_csv(channels_tsv_path, sep='\t')
                bad_channels = channels_data[channels_data['status'] == 'bad']['name'].tolist()
                bad_channels = [ch for ch in bad_channels if isinstance(ch, str)]
                if bad_channels:
                    raw_data.drop_channels(bad_channels)
                    print(f"Dropped bad channels for {subject}, run {run}: {bad_channels}")
            except FileNotFoundError:
                print(f"Channels.tsv not found for {subject}, Run {run}")
                continue

            # Confirm sample rate
            try:
                sampling_frequency = sample_rates[subject][run]
                print(f"Sample rate for {subject}, Run {run}: {sampling_frequency} Hz")
            except KeyError:
                print(f"Sample rate not found for {subject}, Run {run}")
                continue

            # Onset keywords
            try:
                onset_keywords = subject_keywords[subject][run]['onset']
            except KeyError:
                print(f"Onset keywords not found for {subject}, Run {run}")
                continue

            # Read events and crop data
            events_tsv_path = (
                bids_data_path.with_suffix('.tsv')
                .as_posix()
                .replace('_ieeg', '_events')
            )
            try:
                events_data = pd.read_csv(events_tsv_path, sep='\t')
                onset_times = events_data[events_data['trial_type'].isin(onset_keywords)]['sample'].tolist()

                # 30s before/after
                window_size = 30 * sampling_frequency
                for onset_sample in onset_times:
                    start_sample = max(0, onset_sample - window_size)
                    end_sample = onset_sample + window_size

                    cropped = raw_data.copy().crop(
                        tmin=start_sample / sampling_frequency,
                        tmax=end_sample / sampling_frequency
                    )
                    all_raw_data.append(cropped)
                    seizure_windows[f"{subject}_run_{run}_onset_{onset_sample}"] = (start_sample, end_sample)

                    print(f"Cropped data for {subject}, run {run}, onset={onset_sample}: {start_sample}-{end_sample}")
            except FileNotFoundError:
                print(f"Events.tsv file not found for {subject}, run {run}")
                continue

    return all_raw_data, seizure_windows


def adjust_sample_rate(cropped_data_list, target_sampling_rate=250):
    """
    Resample each cropped Raw object to a uniform target sampling rate.

    Parameters
    ----------
    cropped_data_list : list of mne.io.Raw
        List of cropped EEG recordings.
    target_sampling_rate : float
        Desired sampling rate in Hz.
    """
    for idx, cropped_data in enumerate(cropped_data_list):
        original_sf = cropped_data.info['sfreq']
        if original_sf != target_sampling_rate:
            cropped_data.resample(sfreq=target_sampling_rate, npad='auto')
            print(f"Resampled cropped_data #{idx+1} from {original_sf} Hz to {target_sampling_rate} Hz.")
        else:
            print(f"Cropped_data #{idx+1} already at {target_sampling_rate} Hz.")
