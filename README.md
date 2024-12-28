# IUI_EEG_FeatureImplementation

**IUI_EEG_FeatureImplementation** is a modular Python project for detecting High-Frequency Oscillations (HFOs) in EEG data, extracting features around seizure onsets, and training various machine learning models (Random Forest, CatBoost, and Transformers) to classify surgical outcomes. The project uses an MNE-BIDS-compatible folder structure for EEG data and organizes code into several modules for clarity and maintainability.

## Features

1. **Data Reading**
   - Loads `.vhdr` EEG files using MNE.
   - Drops channels marked as “bad”.
   - Crops data around seizure onset times specified in `.tsv` files.

2. **HFO Detection**
   - Bandpass-filters data in the ripple frequency range (e.g., 80–120 Hz).
   - Uses Hilbert transforms to estimate the amplitude envelope.
   - Thresholds each segment’s envelope to detect putative ripples.

3. **Analysis & Feature Extraction**
   - Identifies channels in Seizure Onset Zones (SOZ) vs. non-SOZ from a dictionary (`surgery_outcome_dict`).
   - Selects HFO values at specific percentiles for both SOZ and non-SOZ channels.
   - Persists resulting HFO features in `hfo_data.py`.

4. **Preprocessing**
   - Assembles feature vectors (X) and labels (Y) for machine learning tasks.
   - Offers optional normalization (z-score or min-max) and segment averaging.

5. **Model Training**
   - **Random Forest** and **CatBoost** for classical ML.
   - **Transformers** (BERT-based) for sequence classification via Hugging Face.
   - Provides training metrics (accuracy, F1 score, precision, recall).

6. **Visualization**
   - Creates heatmaps showing HFO counts across channels and time segments.

## Project Structure

```bash
IUI_EEG_FeatureImplementation/
│
├── main2.py                  # Primary script (pipeline orchestrator)
├── main3.py                  # Optional secondary or experimental script
├── run_dictionary.py         # Subject-run mappings & surgery outcomes
├── sample_rates.py           # Sample rate dictionary
├── hfo_data.py               # Generated & updated HFO data dictionary
├── requirements.txt          # Required Python dependencies
├── README.md                 # Project documentation
│
├── EEG_Dataset/              # Your BIDS-like or raw EEG data folder
│   └── ... (.vhdr, .vmrk, .edf, .tsv, etc.)
│
└── src/
    ├── __init__.py           # Makes src a Python package
    ├── data_io.py            # Reading data & adjusting sampling rates
    ├── detection.py          # HFO detection logic
    ├── analysis.py           # Post-processing HFO counts & saving results
    ├── preprocessing.py      # Preparing features & labels for ML
    ├── model_training.py     # Model definitions & training functions
    └── visualization.py      # Plotting & heatmap functionality
