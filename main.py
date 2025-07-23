# main.py

import time
import numpy as np
import argparse
import pickle

# Local modules from src/
from src.data_io import read_data, adjust_sample_rate
from src.detection import detect_hfos_in_segments, group_channels_by_soz
from src.shape_extraction import extract_hfo_waveforms_in_segments
from src.analysis import (
    select_hfo_values_for_specific_percentiles,
    write_hfo_values_to_py,
    events_to_segment_counts
)
from src.preprocessing import prepare_features_and_labels
from src.model_training import (
    train_transformer, train_catboost, train_random_forest
)

# New HFO Detection algorithm

from HFO_Detection_NEW.hilbert_detector import HilbertDetector


from src.visualization import create_hfo_heatmap

# Dictionaries / data
from run_dictionary import subjects_dict, subject_keywords, surgery_outcome_dict
from sample_rates import sample_rates
from hfo_data import hfo_data


def main(train=False, method="count", model_type="catboost"):
    start_time = time.time()

    if train:
        # ===========================
        # Step 1: Read and copy data
        # ===========================
        print("\n=== Reading Data ===")
        base_path = "EEG_Dataset"
        cropped_data_list, seizure_windows = read_data(
            base_path, subjects_dict, subject_keywords, sample_rates
        )

        # Keep a copy of the original data before downsampling
        orig_data_list = [raw.copy() for raw in cropped_data_list]

        print("\n=== Adjust Sample Rate to 250 Hz ===")
        # This modifies cropped_data_list in place, downsampling to 250 Hz
        adjust_sample_rate(cropped_data_list, 250)

        # Prepare the list of (subject, run) tuples in the same order
        flattened_subject_run = [
            (subject, run)
            for subject, runs in subjects_dict.items()
            for run in runs
        ]

        # ================
        # Method: "count"
        # ================
        if method == "count":
            print("\n=== Detect HFO Counts with HilbertDetector ===")

            # ------------------------------------------------------------------
            # 1.  Instantiate detector ONCE with your chosen parameters
            # ------------------------------------------------------------------
            hilbert_det = HilbertDetector(
                fs=250,  # after down-sampling
                low_fc=80,
                high_fc=120,
                threshold=3,
                band_spacing="linear",
                num_bands=300,
                cyc_th=6,
                gap_th=1,
                mp=8  # M3 Max sweet-spot
            )

            # ------------------------------------------------------------------
            # 2.  Loop over runs → per-channel detection & counting
            # ------------------------------------------------------------------

            # --------------------------------------------------------------
            # parameters for segmenting
            # --------------------------------------------------------------
            SEG_LEN_S = 1.0  # seconds per segment
            FS_DS = 250  # your down-sampled rate

            hfo_results = {}  # {run_key: {chan_name: [counts]}}
            hfo_channel_counts = {}  # {run_key: {chan_name: total_events}}

            for raw, (subject, run) in zip(cropped_data_list, flattened_subject_run):

                run_key_str = f"{subject}_{run}"  # e.g. sub-jh101_01
                hfo_results[run_key_str] = {}
                hfo_channel_counts[run_key_str] = {}

                sig_len = raw.n_times  # total samples in this run

                for ch_idx, ch_sig in enumerate(raw.get_data()):
                    ch_name = raw.ch_names[ch_idx]  # "Fz", "C3", ...

                    # 1) detect events on this channel
                    events = hilbert_det.compute(ch_sig)

                    # 2) convert to counts per 1-s segment
                    seg_counts = events_to_segment_counts(events,
                                                          SEG_LEN_S,
                                                          FS_DS,
                                                          sig_len)

                    # 3) store
                    hfo_results[run_key_str][ch_name] = seg_counts
                    hfo_channel_counts[run_key_str][ch_name] = len(events)

                # ---------- console summary ----------
                total = sum(hfo_channel_counts[run_key_str].values())
                top3 = sorted(hfo_channel_counts[run_key_str].items(),
                              key=lambda kv: kv[1], reverse=True)[:3]
                print(f" Detected {total} HFOs in {run_key_str}")
                print("   Top channels (name:count):", top3)

                # ---------- SOZ / non-SOZ grouping ----------
                soz, non_soz = group_channels_by_soz(run_key_str, surgery_outcome_dict)

                all_seg_counts = select_hfo_values_for_specific_percentiles(
                    soz, non_soz, hfo_results, run_key_str
                )

                write_hfo_values_to_py(all_seg_counts,
                                       subject, run, "hfo_data.py")

        # =========================
        # Method: "shape"
        # =========================
        elif method == "shape":
            print("\n=== Extract HFO Waveform Snippets (Shape-Based) ===")
            # cropped_data_list is now at 250 Hz
            # orig_data_list remains at original sampling rate
            hfo_shape_results = extract_hfo_waveforms_in_segments(
                orig_data_list,
                cropped_data_list,
                flattened_subject_run,
                segment_duration=0.5,
                l_freq=80.0,
                h_freq=120.0,
                threshold_factor=4.0,
                snippet_window=0.05
            )

            # Save waveform snippets for later inspection / feature extraction
            output_path = "src/hfo_shape_results.pkl"
            with open(output_path, "wb") as f:
                pickle.dump(hfo_shape_results, f)
            print(f"Saved HFO waveform snippets to '{output_path}'")

        else:
            print(f"Unknown method '{method}'. Choose 'count' or 'shape'.")

    else:
        # ================================
        # Inference/Training on HFO counts
        # ================================
        print("\n=== Preparing Features/Labels ===")
        X, Y = prepare_features_and_labels(
            hfo_data,
            surgery_outcome_dict,
            segment_count=60,
            n_pre=0,
            n_post=30,
            normalize=True,
            normalization_type="min-max",
            averaging_factor=5
        )

        if X.size == 0:
            print("No data available for training.")
            return

        # Map labels: F -> 0, S -> 1
        label_map = {'F': 0, 'S': 1}
        Y_mapped = np.array([label_map[label] for label in Y])

        print(f"\nShapes: X={X.shape}, Y={Y_mapped.shape}")

        # Train or evaluate chosen model
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
    parser = argparse.ArgumentParser(
        description="Run HFO detection (counts) or HFO waveform extraction (shape)."
    )
    parser.add_argument(
        "--train",
        action="store_true",
        help="Process raw EEG data (detect HFOs or extract shapes)."
    )
    parser.add_argument(
        "--method",
        type=str,
        choices=["count", "shape"],
        default="count",
        help="Choose 'count' for HFO-count pipeline or 'shape' for waveform extraction."
    )
    parser.add_argument(
        "--model_type",
        type=str,
        choices=["catboost", "random_forest", "transformer"],
        default="catboost",
        help="Model to train during inference stage (only used when --train is not set)."
    )

    args = parser.parse_args()
    main(train=args.train, method=args.method, model_type=args.model_type)
