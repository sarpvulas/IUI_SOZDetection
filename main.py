import time
import numpy as np
import argparse

# Local modules from src/
from src.data_io import read_data, adjust_sample_rate
from src.detection import detect_hfos_in_segments, group_channels_by_soz
from src.analysis import (
    select_hfo_values_for_specific_percentiles,
    write_hfo_values_to_py
)
from src.preprocessing import prepare_features_and_labels
from src.model_training import (
    train_transformer, train_catboost, train_random_forest
)
from src.visualization import create_hfo_heatmap

# Dictionaries / data
from run_dictionary import subjects_dict, subject_keywords, surgery_outcome_dict
from sample_rates import sample_rates
from hfo_data import hfo_data

def main(train=False, model_type="catboost"):
    start_time = time.time()

    # If train=True, we read raw data & detect HFO -> store in hfo_data
    if train:
        print("\n=== Reading Data ===")
        base_path = "EEG_Dataset"
        cropped_data_list, seizure_windows = read_data(base_path, subjects_dict, subject_keywords, sample_rates)

        print("\n=== Adjust Sample Rate ===")
        adjust_sample_rate(cropped_data_list, 250)

        flattened_subject_run = [
            (subject, run)
            for subject, runs in subjects_dict.items()
            for run in runs
        ]

        print("\n=== Detect HFOs ===")
        hfo_results = detect_hfos_in_segments(cropped_data_list, flattened_subject_run, segment_duration=1)

        # For each run, find SOZ vs. non-SOZ, select percentiles, and write to hfo_data.py
        for idx, run_key in enumerate(hfo_results.keys()):
            subject, run = flattened_subject_run[idx]
            print(f"\nProcessing {run_key} -> subject={subject}, run={run}")

            soz, non_soz = group_channels_by_soz(run_key, surgery_outcome_dict)
            all_segment_results = select_hfo_values_for_specific_percentiles(soz, non_soz, hfo_results, run_key)

            write_hfo_values_to_py(all_segment_results, subject, run, "hfo_data.py")

    else:
        # If train=False, we assume hfo_data.py is already populated with HFO features
        print("\n=== Preparing Features/Labels ===")
        X, Y = prepare_features_and_labels(
            hfo_data,
            surgery_outcome_dict,
            segment_count=60,
            n_pre=0,
            n_post=30,
            normalize=True,
            normalization_type="min-max",
            averaging_factor=10
        )

        if X.size == 0:
            print("No data available for training.")
            return

        # Map labels: F->0, S->1
        label_map = {'F': 0, 'S': 1}
        Y_mapped = np.array([label_map[label] for label in Y])

        print(f"\nShapes: X={X.shape}, Y={Y_mapped.shape}")

        # Train or evaluate
        if model_type == "transformer":
            print("\n--- Using Transformer Model ---")
            train_transformer(X, Y_mapped)
        elif model_type == "random_forest":
            print("\n--- Using RandomForestClassifier ---")
            train_random_forest(X, Y_mapped)
        elif model_type == "catboost":
            print("\n--- Using CatBoostClassifier ---")
            train_catboost(X, Y_mapped)
        else:
            print("Unknown model type:", model_type)

    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time:.3f} seconds.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run HFO detection and model training pipeline.")
    parser.add_argument(
        "--train",
        type=bool,
        default=False,
        help="Flag to indicate whether to process raw EEG data and detect HFOs (True) or use existing data (False)."
    )
    parser.add_argument(
        "--model_type",
        type=str,
        choices=["catboost", "random_forest", "transformer"],
        default="catboost",
        help="The type of model to train (catboost, random_forest, transformer)."
    )

    args = parser.parse_args()
    main(train=args.train, model_type=args.model_type)
