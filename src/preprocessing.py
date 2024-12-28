import numpy as np

def prepare_features_and_labels(
    hfo_data,
    surgery_outcome_dict,
    segment_count,
    n_pre=15,
    n_post=15,
    normalize=False,
    normalization_type="z-score",
    averaging_factor=None
):
    """
    Prepare feature vectors X and label array Y from hfo_data + surgery_outcome_dict.
    Each run has SOZ + Non-SOZ HFO values, shape: (segment_count, 20).

    Returns
    -------
    X : np.ndarray
    Y : np.ndarray
    """
    X, Y = [], []
    total_segments = n_pre + n_post

    if averaging_factor:
        # Make total_segments divisible by averaging_factor
        adjusted_total = (total_segments // averaging_factor) * averaging_factor
        if total_segments % averaging_factor != 0:
            print(f"Adjusting total segments from {total_segments} to {adjusted_total}")
        total_segments = adjusted_total

    # Each segment has 20 values (10 percentile for SOZ + 10 for non-SOZ)
    required_length = ((total_segments // averaging_factor) if averaging_factor else total_segments) * 20

    for subject, runs in hfo_data.items():
        for run, data in runs.items():
            key = (subject, run.zfill(2))
            if key not in surgery_outcome_dict:
                continue

            doc_info = surgery_outcome_dict[key]
            outcome = doc_info.get("surgery_outcome")
            if outcome not in ["F", "S"]:
                continue

            soz_arr = np.array(data["SOZ Percentiles"])      # shape: (segment_count, 10)
            non_soz_arr = np.array(data["Non-SOZ Percentiles"])  # shape: (segment_count, 10)

            # Check for enough segments
            if soz_arr.shape[0] < total_segments or non_soz_arr.shape[0] < total_segments:
                print(f"Skipping {subject} {run}: not enough segments.")
                continue

            # Seizure assumed in middle
            seizure_idx = segment_count // 2
            start_idx = max(0, seizure_idx - n_pre)
            end_idx = min(segment_count, seizure_idx + n_post)

            soz_focus = soz_arr[start_idx:end_idx]
            non_soz_focus = non_soz_arr[start_idx:end_idx]

            # Ensure same length
            min_len = min(len(soz_focus), len(non_soz_focus))
            soz_focus = soz_focus[:min_len]
            non_soz_focus = non_soz_focus[:min_len]

            # Normalization
            if normalize:
                if normalization_type == "z-score":
                    soz_focus = (soz_focus - soz_focus.mean()) / (soz_focus.std() + 1e-8)
                    non_soz_focus = (non_soz_focus - non_soz_focus.mean()) / (non_soz_focus.std() + 1e-8)
                elif normalization_type == "min-max":
                    s_min, s_max = soz_focus.min(), soz_focus.max()
                    soz_focus = (soz_focus - s_min) / (s_max - s_min + 1e-8)
                    n_min, n_max = non_soz_focus.min(), non_soz_focus.max()
                    non_soz_focus = (non_soz_focus - n_min) / (n_max - n_min + 1e-8)
                else:
                    raise ValueError("Invalid normalization_type")

            # Segment averaging
            if averaging_factor:
                def avg_segments(d, factor):
                    length = d.shape[0] - (d.shape[0] % factor)
                    return d[:length].reshape(-1, factor, d.shape[1]).mean(axis=1)

                soz_focus = avg_segments(soz_focus, averaging_factor)
                non_soz_focus = avg_segments(non_soz_focus, averaging_factor)

            combined_features = np.concatenate([soz_focus.flatten(), non_soz_focus.flatten()])
            if combined_features.shape[0] == required_length:
                X.append(combined_features)
                Y.append(outcome)
            else:
                print(f"Dropping {subject} {run}: length mismatch {combined_features.shape[0]} != {required_length}")

    X = np.array(X)
    Y = np.array(Y)
    print(f"Final shape of X: {X.shape}, Y: {Y.shape}")
    return X, Y
