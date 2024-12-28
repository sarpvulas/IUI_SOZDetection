from run_dictionary import subjects_dict  # Subjects as keys, runs as values
from run_dictionary import subject_keywords
from run_dictionary import surgery_outcome_dict
from sample_rates import sample_rates
from entropy_features import entropy_features
import pandas as pd
import warnings
import time
import mne
import matplotlib.pyplot as plt
from mne_bids import BIDSPath
import numpy as np
from scipy.signal import hilbert, stft
from scipy.signal.windows import hann
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score, precision_score, recall_score
from xgboost import XGBClassifier
from rerf.rerfClassifier import rerfClassifier
from catboost import CatBoostClassifier
import pprint  # Add this import at the top of your file if not already present
import sys
from sklearn.model_selection import LeaveOneOut


# Suppress specific warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Constants
base_path = "EEG_Dataset"
FREQUENCY_BANDS = {
    'delta': (1, 3),
    'theta': (4, 7),
    'alpha': (8, 13),
    'beta': (14, 30),
    'gamma': (31, 50)
}

start_time = time.time()

def read_data():
    counter = 0
    all_raw_data = []  # List to store cropped raw data for all subjects and runs
    seizure_windows = {}  # Dictionary to store seizure windows for each subject and run

    for subject, runs in subjects_dict.items():
        for run in runs:
            counter += 1

            # Create the BIDS path
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

            # Add the 'ieeg' folder manually to the path
            bids_data_path = bids_data_path.directory / "ieeg" / bids_data_path.basename

            print("Subject:", subject, ", run:", run, ", recording number:", counter, "\n")

            # Read the data using the .vhdr file
            try:
                raw_data = mne.io.read_raw_brainvision(str(bids_data_path), preload=True)
            except FileNotFoundError:
                print(f"\nFile not found for Subject {subject}, Run {run}")
                continue

            # Construct the channels.tsv file path
            channels_tsv_path = bids_data_path.with_suffix('.tsv').as_posix().replace('_ieeg', '_channels')

            # Initialize channel list for this subject and run
            try:
                channels_data = pd.read_csv(channels_tsv_path, sep='\t')

                # Filter out the channels that are marked as bad
                bad_channels = channels_data[channels_data['status'] == 'bad']['name'].tolist()
                bad_channels = [ch for ch in bad_channels if isinstance(ch, str)]  # Ensure valid channel names
                print(f"Bad channels for {subject}, Run {run}: {bad_channels}")

                # Drop bad channels from raw_data if there are any
                if bad_channels:
                    raw_data.drop_channels(bad_channels)
                    print(f"Dropped bad channels: {bad_channels}")
            except FileNotFoundError:
                print(f"\nChannels.tsv file not found for Subject {subject}, Run {run}")
                continue

            # Get the sample rate for the current run
            try:
                sampling_frequency = sample_rates[subject][run]
                print(f"Sample rate for {subject}, Run {run}: {sampling_frequency} Hz")
            except KeyError:
                print(f"Sample rate not found for {subject}, Run {run}")
                continue

            # Get the correct onset keyword for the current subject and run from subject_keywords
            try:
                onset_keywords = subject_keywords[subject][run]['onset']
            except KeyError:
                print(f"\nKeywords not found for Subject {subject}, Run {run}")
                continue

            # Construct the events TSV file path
            events_tsv_path = bids_data_path.with_suffix('.tsv').as_posix().replace('_ieeg', '_events')

            # Check if the events.tsv file exists
            try:
                # Read the events.tsv file
                events_data = pd.read_csv(events_tsv_path, sep='\t')

                # Filter the events_data based on the onset keywords
                onset_times = events_data[events_data['trial_type'].isin(onset_keywords)]['sample'].tolist()

                # Calculate the window size based on the sampling frequency (30 seconds before and after)
                window_size = 30 * sampling_frequency  # 30 seconds in samples

                # Crop the data 30 seconds before and after each onset time
                for onset_sample in onset_times:
                    start_sample = max(0, onset_sample - window_size)  # Ensure start is not negative
                    end_sample = onset_sample + window_size

                    # Crop the raw data to this window
                    cropped_data = raw_data.copy().crop(tmin=start_sample / sampling_frequency, 
                                                        tmax=end_sample / sampling_frequency)

                    # Store the cropped data and seizure window information
                    all_raw_data.append(cropped_data)
                    seizure_windows[f"{subject}_run_{run}_onset_{onset_sample}"] = (start_sample, end_sample)

                    print(f"Cropping data for Subject {subject}, Run {run}, Onset Sample {onset_sample}: "
                          f"{start_sample} to {end_sample} samples")

            except FileNotFoundError:
                print(f"\nEvents.tsv file not found for Subject {subject}, Run {run}")
                continue

    return all_raw_data, seizure_windows

def adjust_sample_rate(cropped_data_list, target_sampling_rate):

    for idx, cropped_data in enumerate(cropped_data_list):
        original_sampling_rate = cropped_data.info['sfreq']  # Get the current sampling rate
        print(f"Original sampling rate for cropped_data {idx + 1}: {original_sampling_rate} Hz")

        if original_sampling_rate != target_sampling_rate:
            # Resample the data to the target sampling rate
            cropped_data.resample(sfreq=target_sampling_rate, npad='auto')
            print(f"Cropped_data {idx + 1} resampled to {target_sampling_rate} Hz")

        # Check the new sampling rate after resampling
        new_sampling_rate = cropped_data.info['sfreq']
        print(f"New sampling rate for cropped_data {idx + 1}: {new_sampling_rate} Hz")

def detect_hfos_in_segments(cropped_data_list, flattened_subject_run, segment_duration=1, l_freq=80, h_freq=120, threshold_factor=4):
    """
    Detect HFOs (ripples) in segments for each channel in the given cropped EEG data.

    Parameters:
    - cropped_data_list: list of MNE Raw objects containing cropped EEG data (downsampled to 250 Hz)
    - flattened_subject_run: list of (subject, run) tuples in the order of cropped_data_list
    - segment_duration: the duration of each segment in seconds (default is 1 second)
    - l_freq: lower bound for the HFO band (default is 80 Hz for ripples)
    - h_freq: upper bound for the HFO band (default is 120 Hz)
    - threshold_factor: factor to set the threshold based on the standard deviation (default is 4)

    Returns:
    - hfo_results: a dictionary where each entry contains the detected HFO events for each segment and each channel.
    """
    hfo_results = {}

    for idx, cropped_data in enumerate(cropped_data_list):
        # Use the corresponding subject and run from flattened_subject_run
        subject, run = flattened_subject_run[idx]
        run_key = f"{subject}_{run}"  # Create run_key from subject and run
        hfo_results[run_key] = {}

        # Get the sampling frequency and calculate the number of samples per segment
        sfreq = cropped_data.info['sfreq']
        segment_samples = int(segment_duration * sfreq)

        print(f"\nProcessing {run_key} with sampling frequency: {sfreq} Hz and segment duration: {segment_duration} seconds.")
        print(f"Each segment will have {segment_samples} samples.")

        for channel_idx, channel_name in enumerate(cropped_data.ch_names):
            channel_data = cropped_data.get_data(picks=channel_idx)[0]
            print(f"\nProcessing Channel: {channel_name} (Index: {channel_idx})")

            # Check if channel contains valid (non-zero, non-NaN) values
            if np.all(channel_data == 0) or np.any(np.isnan(channel_data)):
                print(f"WARNING: Channel {channel_name} contains only zeros or NaNs!")
                continue

            total_samples = channel_data.shape[0]
            num_segments = total_samples // segment_samples
            hfo_results[run_key][channel_name] = []

            for segment_idx in range(num_segments):
                start_idx = segment_idx * segment_samples
                end_idx = start_idx + segment_samples
                segment_data = channel_data[start_idx:end_idx]

                # Bandpass filter the data for HFO detection
                hfo_band_data = mne.filter.filter_data(segment_data, sfreq=sfreq, 
                                                       l_freq=l_freq, h_freq=h_freq, method='fir', fir_design='firwin')
                # Calculate the envelope using Hilbert transform
                hfo_envelope = np.abs(hilbert(hfo_band_data))

                # Set a threshold based on the standard deviation of the envelope
                threshold = np.mean(hfo_envelope) + threshold_factor * np.std(hfo_envelope)

                # Detect points where HFO exceeds the threshold
                hfo_events = np.where(hfo_envelope > threshold)

                hfo_count = len(hfo_events[0])
                hfo_results[run_key][channel_name].append(hfo_count if hfo_count > 0 else 0)

    print(f"\nHFO results for all runs: {hfo_results}")
    return hfo_results

def calculate_differential_entropy(data, fs=250, num_bands=5):
    """ 
    Calculate differential entropy for specified frequency bands using STFT 
    and ensure exactly `num_bands` features per segment.
    """
    nperseg = 250  # Window size
    if data.shape[0] < nperseg:
        # Pad data if shorter than the window
        data = np.pad(data, (0, nperseg - data.shape[0]), mode='constant', constant_values=(0, 0))
    
    # Apply STFT
    window = hann(nperseg, sym=False)
    freqs, _, Zxx = stft(data, fs=fs, window=window, nperseg=nperseg, noverlap=0, boundary=None)
    psd = np.abs(Zxx) ** 2 / nperseg  # Compute power spectral density (PSD)

    de_features = []
    for band, (low, high) in FREQUENCY_BANDS.items():
        idx = (freqs >= low) & (freqs <= high)
        band_psd = psd[idx, :]
        band_de = np.log(np.sum(band_psd, axis=0) + 1e-8)  # Sum power in the band and log
        
        # If the result doesn't have enough values, pad with -1
        if len(band_de) < num_bands:
            band_de = np.concatenate([band_de, [-1] * (num_bands - len(band_de))])
        else:
            band_de = band_de[:num_bands]  # Trim to ensure exactly num_bands values
        

        de_features.append(band_de)

    return np.concatenate(de_features)  # Return as a flattened array

def extract_entropy_features(cropped_data_list, flattened_subject_run):
    """
    Extract differential entropy (DE) features for each subject and run.

    Parameters:
    - cropped_data_list: list of MNE Raw objects containing cropped EEG data
    - flattened_subject_run: list of (subject, run) tuples in the order of cropped_data_list
    
    Returns:
    - entropy_features: dictionary containing DE features per subject and run
    """
    entropy_features = {}
    
    for idx, cropped_data in enumerate(cropped_data_list):
        subject, run = flattened_subject_run[idx]
        run_key = f"{subject}_{run}"
        entropy_features[run_key] = {}

        for channel_idx, channel_name in enumerate(cropped_data.ch_names):
            channel_data = cropped_data.get_data(picks=channel_idx)[0]
            sfreq = cropped_data.info['sfreq']

            # Calculate differential entropy for the channel
            de_feature = calculate_differential_entropy(channel_data, fs=sfreq)
            entropy_features[run_key][channel_name] = de_feature

    
    return entropy_features

def group_channels_by_soz(run_key, surgery_outcome_dict):
    """
    Group the channels into SOZ and non-SOZ based on the doctor's prediction from the surgery_outcome_dict.
    """
    subject, run_num = run_key.split('_')  # `run_key` is a string formatted as "subject_run"

    # Debugging info
    print(f"subject: {subject}")
    
    print(f"run: {run_num}")
    
    print("Keys in surgery_outcome_dict:", surgery_outcome_dict.keys())
    
    # Fetch the entry for the subject and run from surgery_outcome_dict
    doc_info = surgery_outcome_dict.get((subject, run_num.zfill(2)), {})  # Ensure run number is 2 digits

    if not doc_info:
        print(f"No matching entry for {subject}, Run {run_num.zfill(2)} in surgery_outcome_dict.")
        return [], []

    all_channels = doc_info.get('channels', [])
    soz_channels = doc_info.get('soz_channels', [])
    non_soz_channels = [ch for ch in all_channels if ch not in soz_channels]

    return soz_channels, non_soz_channels

def combine_hfo_and_entropy_features(run_key, hfo_results, entropy_features, soz_channels, non_soz_channels):
    """
    Combine HFO and DE features for SOZ and Non-SOZ channels with percentile sampling.

    Parameters:
        run_key (str): Run key identifying the current run.
        hfo_results (dict): HFO results per channel and segment.
        entropy_features (dict): Differential entropy features per channel and segment.
        soz_channels (list): List of SOZ channels.
        non_soz_channels (list): List of non-SOZ channels.

    Returns:
        dict: Combined features for the run with SOZ and non-SOZ grouped features.
    """
    # Check if the run_key exists in hfo_results and entropy_features
    if run_key not in hfo_results or run_key not in entropy_features:
        print(f"[WARNING] No matching entry for {run_key} in hfo_results or entropy_features.")
        return None  # Skip this run

    combined_results = {"SOZ Percentiles": [], "Non-SOZ Percentiles": []}
    num_segments = len(next(iter(hfo_results[run_key].values()), []))  # Handle empty channels gracefully
    percentiles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Filter valid channels
    valid_soz_channels = [ch for ch in soz_channels if ch in hfo_results[run_key] and ch in entropy_features[run_key]]
    valid_non_soz_channels = [ch for ch in non_soz_channels if ch in hfo_results[run_key] and ch in entropy_features[run_key]]

    # Debugging: Print channel information
    print(f"[DEBUG] Run: {run_key}")
    print(f"[DEBUG] Valid SOZ Channels: {len(valid_soz_channels)}")
    print(f"[DEBUG] Valid Non-SOZ Channels: {len(valid_non_soz_channels)}")

    # Skip if there are no valid SOZ or Non-SOZ channels
    if not valid_soz_channels and not valid_non_soz_channels:
        print(f"[WARNING] No valid SOZ or Non-SOZ channels for {run_key}. Skipping.")
        return None

    for segment_idx in range(num_segments):
        # Collect raw values for HFO and DE
        soz_hfo_values = [hfo_results[run_key][channel][segment_idx] for channel in valid_soz_channels]
        soz_de_values = [entropy_features[run_key][channel][segment_idx] for channel in valid_soz_channels]
        non_soz_hfo_values = [hfo_results[run_key][channel][segment_idx] for channel in valid_non_soz_channels]
        non_soz_de_values = [entropy_features[run_key][channel][segment_idx] for channel in valid_non_soz_channels]

        # Debugging: Print raw HFO and DE values
        print(f"[DEBUG] Segment {segment_idx}, SOZ HFO Raw Values: {soz_hfo_values}")
        print(f"[DEBUG] Segment {segment_idx}, SOZ DE Raw Values: {soz_de_values}")
        print(f"[DEBUG] Segment {segment_idx}, Non-SOZ HFO Raw Values: {non_soz_hfo_values}")
        print(f"[DEBUG] Segment {segment_idx}, Non-SOZ DE Raw Values: {non_soz_de_values}")

        # Skip this segment if no values are available
        if not soz_hfo_values and not non_soz_hfo_values:
            print(f"[WARNING] No valid HFO values for segment {segment_idx}. Skipping segment.")
            continue

        # Apply percentile sampling for SOZ
        soz_hfo_sampled = [np.percentile(soz_hfo_values, p) for p in percentiles] if soz_hfo_values else [0] * len(percentiles)
        soz_de_sampled = []
        for p in percentiles:
            if soz_hfo_values:
                closest_de = [entropy_features[run_key][channel][segment_idx]
                              for channel in valid_soz_channels
                              if hfo_results[run_key][channel][segment_idx] >= np.percentile(soz_hfo_values, p)]
                soz_de_sampled.extend(closest_de[:5])  # Ensure 5 DE per HFO percentile

        # Apply percentile sampling for Non-SOZ
        non_soz_hfo_sampled = [np.percentile(non_soz_hfo_values, p) for p in percentiles] if non_soz_hfo_values else [0] * len(percentiles)
        non_soz_de_sampled = []
        for p in percentiles:
            if non_soz_hfo_values:
                closest_de = [entropy_features[run_key][channel][segment_idx]
                              for channel in valid_non_soz_channels
                              if hfo_results[run_key][channel][segment_idx] >= np.percentile(non_soz_hfo_values, p)]
                non_soz_de_sampled.extend(closest_de[:5])  # Ensure 5 DE per HFO percentile

        # Combine results
        combined_results["SOZ Percentiles"].append(soz_hfo_sampled + soz_de_sampled[:50])
        combined_results["Non-SOZ Percentiles"].append(non_soz_hfo_sampled + non_soz_de_sampled[:50])

    return combined_results

def write_hfo_values_to_py(all_segment_results, subject, run, output_file="hfo_data.py"):
    """
    Write the selected SOZ and Non-SOZ HFO values into a Python file for each subject and run 
    in a nested dictionary structure, maintaining previously written data.

    Parameters:
    - all_segment_results: List of SOZ and Non-SOZ HFO values for each segment
    - subject: The subject identifier (e.g., 'sub-jh101')
    - run: The run number (e.g., '01')
    - output_file: Name of the output Python file (default is 'hfo_data.py')
    """
    # Prepare data to write as a nested dictionary
    new_data = {
        subject: {
            run: {
                'SOZ Percentiles': [segment["soz"] for segment in all_segment_results],
                'Non-SOZ Percentiles': [segment["non_soz"] for segment in all_segment_results]
            }
        }
    }

    try:
        # Try to load existing data from the output file if it exists
        with open(output_file, "r") as f:
            file_content = f.read()
            if "hfo_data =" in file_content:
                hfo_data = eval(file_content.split("hfo_data =")[1].strip())
            else:
                hfo_data = {}
    except FileNotFoundError:
        # If the file does not exist, start with an empty dictionary
        hfo_data = {}

    # Merge new data with existing data
    if subject in hfo_data:
        hfo_data[subject].update(new_data[subject])
    else:
        hfo_data.update(new_data)

    # Write the updated hfo_data back to the file
    with open(output_file, "w") as f:
        f.write(f"hfo_data = {hfo_data}\n")

    print(f"Data for {subject} run {run} has been written to {output_file}")



def prepare_combined_features_and_labels(
        entropy_data, 
        surgery_outcome_dict, 
        segment_count=60, 
        num_channels=20, 
        num_bands=5, 
        use_only_hfo=True
    ):
    """
    Prepare combined features and labels for model training.

    Parameters:
    - entropy_data: Dictionary containing SOZ and Non-SOZ percentile data.
    - surgery_outcome_dict: Dictionary with surgery outcomes for subjects.
    - segment_count: Number of segments per subject.
    - num_channels: Total number of channels.
    - num_bands: Number of frequency bands for DE.
    - use_only_hfo: Boolean flag to use only HFO values in the features.

    Returns:
    - X: Numpy array of combined features.
    - Y: Numpy array of corresponding labels.
    """
    X = []
    Y = []

    # Define feature lengths
    hfo_length_per_segment = num_channels // 2  # HFO for half the channels (SOZ or Non-SOZ)
    de_length_per_segment = 0 if use_only_hfo else (num_channels // 2) * num_bands  # DE if not using only HFO
    segment_feature_length = 2 * (hfo_length_per_segment + de_length_per_segment)  # SOZ + Non-SOZ
    total_required_length = segment_count * segment_feature_length

    print(f"Expected total feature length per subject: {total_required_length}")
    input("[STOP] Verify expected lengths... Press Enter to continue.")

    for subject, runs in entropy_data.items():
        print(f"Processing subject: {subject}")
        if runs is None or "Non-SOZ Percentiles" not in runs or "SOZ Percentiles" not in runs:
            print(f"  Skipping subject {subject} due to missing runs or required percentile data.")
            continue

        # Extract surgery outcome
        surgery_key = (subject.split('_')[0], subject.split('_')[1])  # Tuple of subject base and run
        surgery_info = surgery_outcome_dict.get(surgery_key, None)

        if surgery_info is None:
            print(f"  Skipping subject {subject} due to missing surgery outcome information for {surgery_key}.")
            continue

        surgery_outcome = surgery_info.get('surgery_outcome', None)
        if surgery_outcome not in ['F', 'S']:
            print(f"  Skipping subject {subject} due to unsupported surgery outcome: {surgery_outcome}")
            continue

        combined_features = []

        # Combine SOZ and Non-SOZ features segment by segment
        soz_segments = runs["SOZ Percentiles"]
        non_soz_segments = runs["Non-SOZ Percentiles"]

        if len(soz_segments) != segment_count or len(non_soz_segments) != segment_count:
            print(f"  Skipping subject {subject} due to mismatched segment counts.")
            continue

        for segment_idx in range(segment_count):
            soz_segment = soz_segments[segment_idx]
            non_soz_segment = non_soz_segments[segment_idx]

            # Extract only HFO if specified
            if use_only_hfo:
                soz_segment = soz_segment[:hfo_length_per_segment]
                non_soz_segment = non_soz_segment[:hfo_length_per_segment]
            else:
                # Validate SOZ features
                if len(soz_segment) != hfo_length_per_segment + de_length_per_segment:
                    print(f"      Invalid SOZ feature length in segment {segment_idx} for subject {subject}. Padding with -1.")
                    soz_segment = soz_segment[:hfo_length_per_segment + de_length_per_segment] + \
                                  [-1] * ((hfo_length_per_segment + de_length_per_segment) - len(soz_segment))

                # Validate Non-SOZ features
                if len(non_soz_segment) != hfo_length_per_segment + de_length_per_segment:
                    print(f"      Invalid Non-SOZ feature length in segment {segment_idx} for subject {subject}. Padding with -1.")
                    non_soz_segment = non_soz_segment[:hfo_length_per_segment + de_length_per_segment] + \
                                      [-1] * ((hfo_length_per_segment + de_length_per_segment) - len(non_soz_segment))

            # Combine SOZ and Non-SOZ features for the segment
            segment_combined = soz_segment + non_soz_segment
            combined_features.extend(segment_combined)

        if len(combined_features) == total_required_length:
            X.append(combined_features)
            Y.append(surgery_outcome)
            print(f"  Successfully added combined SOZ and Non-SOZ features for subject {subject}.")
        else:
            print(f"  Skipping subject {subject} due to incorrect combined feature length: {len(combined_features)}")

    # Filter out invalid entries
    filtered_X = []
    filtered_Y = []

    for i, features in enumerate(X):
        if len(features) == total_required_length:
            filtered_X.append(features)
            filtered_Y.append(Y[i])
        else:
            print(f"[DEBUG] Dropping entry {i} with length {len(features)}")

    # Convert to numpy arrays
    X = np.array(filtered_X)
    Y = np.array(filtered_Y)

    print(f"Final shape of X: {X.shape}, Y: {Y.shape}")
    np.set_printoptions(threshold=sys.maxsize)
    print(X[0][:200])
    input("[STOP] Verify final dataset structure... Press Enter to continue.")

    return X, Y

    # Convert lists to numpy arrays

def extract_entropy_features(cropped_data_list, flattened_subject_run, normalize=True):
    """
    Extract differential entropy (DE) features for each subject and run.

    Parameters:
    - cropped_data_list: list of MNE Raw objects containing cropped EEG data
    - flattened_subject_run: list of (subject, run) tuples in the order of cropped_data_list
    - normalize: boolean flag to normalize DE features per channel (default=False)

    Returns:
    - entropy_features: dictionary containing DE features per subject and channel
    """
    entropy_features = {}
    for idx, cropped_data in enumerate(cropped_data_list):
        subject, run = flattened_subject_run[idx]
        run_key = f"{subject}_{run}"
        entropy_features[run_key] = {}

        for channel_idx, channel_name in enumerate(cropped_data.ch_names):
            channel_data = cropped_data.get_data(picks=channel_idx)[0]
            sfreq = cropped_data.info['sfreq']
            segment_samples = int(sfreq)
            num_segments = len(channel_data) // segment_samples

            channel_entropy_features = []
            for seg in range(num_segments):
                start_idx = seg * segment_samples
                end_idx = start_idx + segment_samples
                segment_data = channel_data[start_idx:end_idx]

                de_feature = calculate_differential_entropy(segment_data, fs=sfreq)
                channel_entropy_features.append(de_feature)

            if channel_entropy_features:
                channel_entropy_features = np.concatenate(channel_entropy_features)
                if normalize:
                    max_abs_value = np.max(np.abs(channel_entropy_features)) if np.max(np.abs(channel_entropy_features)) != 0 else 1
                    channel_entropy_features /= max_abs_value
            else:
                channel_entropy_features = np.zeros(len(FREQUENCY_BANDS))

            entropy_features[run_key][channel_name] = channel_entropy_features

    return entropy_features

def evaluate_model(Y_test, Y_pred):
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%")
    f1 = f1_score(Y_test, Y_pred, average='weighted')
    precision = precision_score(Y_test, Y_pred, average='weighted')
    recall = recall_score(Y_test, Y_pred, average='weighted')
    print(f"F1 Score: {f1:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    conf_matrix = confusion_matrix(Y_test, Y_pred)
    print("Confusion Matrix:")
    print(conf_matrix)
    print("Classification Report:")
    print(classification_report(Y_test, Y_pred))


def save_combined_features(combined_features, output_file="features_data.py"):
    """
    Save combined HFO and DE features to a Python file.

    Parameters:
        combined_features (dict): Combined features with HFO and DE for each run.
        output_file (str): File to save the features.
    """
    with open(output_file, "w") as f:
        f.write("features_data = ")
        pprint.pprint(combined_features, stream=f, width=120)

    print(f"Combined HFO and DE features have been saved to {output_file} in a structured format.")

def initialize_classifier(classifier_type):
    if classifier_type == "random_forest":
        return RandomForestClassifier(
            max_depth=10, max_features='sqrt', min_samples_split=10,
            n_estimators=50, random_state=42
        )
    elif classifier_type == "rerf":
        return rerfClassifier(
            projection_matrix="S-RerF", n_estimators=500, max_features="auto", feature_combinations=1.5,
            n_jobs=-1, random_state=42, image_height=1, patch_height_max=1, patch_height_min=1, 
            patch_width_max=16, patch_width_min=1, max_depth=6, min_samples_split=2, image_width=60
        )
    elif classifier_type == "catboost":
        return CatBoostClassifier(
            iterations=500, depth=6, learning_rate=0.1, loss_function='Logloss',
            random_seed=42, verbose=0
        )
    elif classifier_type == "xgboost":
        return XGBClassifier(
            n_estimators=100, max_depth=6, learning_rate=0.1, random_state=42,
            use_label_encoder=False, eval_metric='logloss'
        )
    else:
        raise ValueError(f"Unsupported classifier type: {classifier_type}")


def main(surgery_outcome_dict, train, classifier_type="catboost", use_loocv=True):
    if train:
        # Full training mode, generating both HFO and DE features
        cropped_data_list, _ = read_data()
        target_sampling_rate = 250
        adjust_sample_rate(cropped_data_list, target_sampling_rate)
        flattened_subject_run = [(subject, run) for subject, runs in subjects_dict.items() for run in runs]
        
        # Detect HFOs and extract entropy features separately
        hfo_results = detect_hfos_in_segments(cropped_data_list, flattened_subject_run, segment_duration=1)
        entropy_features = extract_entropy_features(cropped_data_list, flattened_subject_run)
        
        combined_features = {}

        # Iterate over all runs and process HFO + DE features
        for idx, run_key in enumerate(hfo_results):
            subject, run = flattened_subject_run[idx]

            # Group channels by SOZ and non-SOZ
            soz_channels, non_soz_channels = group_channels_by_soz(run_key, surgery_outcome_dict)

            # Combine HFO and DE features for SOZ and Non-SOZ channels
            combined_features[run_key] = combine_hfo_and_entropy_features(
                run_key,
                hfo_results,
                entropy_features,
                soz_channels,
                non_soz_channels
            )

        # Save the combined features in a structured format
        save_combined_features(combined_features, output_file="features_data.py")

    else:
        # Prepare features and labels with loaded features_data
        from features_data import features_data

        X, Y = prepare_combined_features_and_labels(features_data, surgery_outcome_dict, segment_count=60)
        
        if X.size == 0:
            print("No data available for training.")
            return
        
        label_mapping = {'F': 0, 'S': 1}
        Y = np.array([label_mapping[label] for label in Y])

        if use_loocv:
            # Perform LOOCV
            from sklearn.model_selection import LeaveOneOut
            loo = LeaveOneOut()
            predictions = []
            true_labels = []

            for train_index, test_index in loo.split(X):
                X_train, X_test = X[train_index], X[test_index]
                Y_train, Y_test = Y[train_index], Y[test_index]

                clf = initialize_classifier(classifier_type)
                clf.fit(X_train, Y_train)
                pred = clf.predict(X_test)

                predictions.append(pred[0])
                true_labels.append(Y_test[0])

            # Evaluate LOOCV results
            acc = accuracy_score(true_labels, predictions)
            f1 = f1_score(true_labels, predictions, average="weighted")

            print("\nLOOCV Results:")
            print(f"Accuracy: {acc:.2f}")
            print(f"F1 Score: {f1:.2f}")
        else:
            # Perform regular train-test split
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

            clf = initialize_classifier(classifier_type)
            clf.fit(X_train, Y_train)
            Y_pred = clf.predict(X_test)

            # Evaluate regular train-test split results
            evaluate_model(Y_test, Y_pred)

def create_hfo_heatmap(hfo_results, run_key='cropped_data_1'):
    """
    Create a heatmap of HFO counts for the specified run, where rows represent channels and columns represent segments.

    Parameters:
    - hfo_results: dictionary containing HFO counts for each segment and each channel
    - run_key: the key for the run to visualize (default is 'cropped_data_1')
    """
    run_data = hfo_results.get(run_key, {})
    heatmap_data = []

    for channel_name, hfo_counts in run_data.items():
        heatmap_data.append(hfo_counts)  # Each row is HFO counts for a channel

    heatmap_df = pd.DataFrame(heatmap_data, index=run_data.keys(), columns=[f"Segment {i+1}" for i in range(len(hfo_counts))])
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_df, annot=False, cmap='coolwarm', cbar=True)
    plt.title(f'HFO Heatmap for {run_key}')
    plt.xlabel('Segments')
    plt.ylabel('Channels')
    plt.show()

# Run the main function and optional heatmap visualization
main(surgery_outcome_dict, train=False)

# Optionally, create the heatmap for HFO results
# create_hfo_heatmap(hfo_results, run_key='cropped_data_1')

end_time = time.time()
print("Total execution time: ", "{0:.3g}".format(end_time - start_time), " seconds.\n")
