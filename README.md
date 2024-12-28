# IUI_EEG_FeatureImplementation

**IUI_EEG_FeatureImplementation** is a modular Python project for detecting High-Frequency Oscillations (HFOs) in EEG data, extracting features around seizure onsets, and training various machine learning models (Random Forest, CatBoost, and Transformers) to classify surgical outcomes. The project uses an MNE-BIDS-compatible folder structure for EEG data and organizes code into several modules for clarity and maintainability.

## Features

1. **Data Reading**
   - Loads `.vhdr` EEG files using MNE.
   - Drops channels marked as “bad”.
   - Crops data around seizure onset times specified in `.tsv` files.
   - Handles EEG data in the context of pre-defined time windows for seizure events.

2. **HFO Detection**
   - Bandpass-filters data in the ripple frequency range (e.g., 80–120 Hz).
   - Uses Hilbert transforms to estimate the amplitude envelope.
   - Thresholds each segment’s envelope to detect putative ripples.
   - Supports parameter tuning for HFO detection thresholds and frequency ranges.

3. **Analysis & Feature Extraction**
   - Identifies channels in Seizure Onset Zones (SOZ) vs. non-SOZ from a dictionary (`surgery_outcome_dict`).
   - Selects HFO values at specific percentiles for both SOZ and non-SOZ channels.
   - Calculates additional statistical measures (mean, variance, skewness, kurtosis) for feature enrichment.
   - Persists resulting HFO features in `hfo_data.py`.

4. **Preprocessing**
   - Assembles feature vectors (X) and labels (Y) for machine learning tasks.
   - Offers optional normalization (z-score or min-max) and segment averaging.
   - Implements dimensionality reduction (e.g., PCA) for feature selection.

5. **Model Training**
   - **Random Forest** and **CatBoost** for classical ML.
   - **Transformers** (BERT-based) for sequence classification via Hugging Face.
   - Integrates Differential Entropy features with HFO features for advanced model training.
   - Provides training metrics (accuracy, F1 score, precision, recall).

6. **Evaluation & Testing**
   - Implements cross-validation for model robustness.
   - Includes options for testing models with Differential Entropy and HFO features combined or separately.
   - Generates comprehensive evaluation reports including confusion matrices.

7. **Visualization**
   - Creates heatmaps showing HFO counts across channels and time segments.
   - Visualizes feature distributions for SOZ and non-SOZ channels.
   - Supports interactive plots for channel-wise analysis.

8. **Modularity**
   - Easy integration with other projects through modular design.
   - Includes configuration files for parameter tuning and reproducibility.

## Project Structure

```bash
IUI_EEG_FeatureImplementation/
│
├── main2.py                  # Primary script (pipeline orchestrator)
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
    ├── evaluation.py         # Model evaluation and report generation
    └── visualization.py      # Plotting & heatmap functionality
```

## Dependencies

Ensure the following Python packages are installed:

- `numpy`
- `scipy`
- `pandas`
- `matplotlib`
- `mne`
- `scikit-learn`
- `catboost`
- `transformers`
- `torch`
- `seaborn`

Install dependencies via:
```bash
pip install -r requirements.txt
```

## Usage

### Run the Pipeline with Arguments
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/IUI_EEG_FeatureImplementation.git
   cd IUI_EEG_FeatureImplementation
   ```
2. Prepare the EEG dataset following the MNE-BIDS structure.
3. Edit `run_dictionary.py` to include subject-run mappings and surgery outcomes.
4. Run the script with `argparse` options:

   To process raw EEG data and detect HFOs:
   ```bash
   python main2.py --train True --model_type catboost
   ```

   To train a model using existing HFO data:
   ```bash
   python main2.py --train False --model_type random_forest
   ```

   To use the Transformer model:
   ```bash
   python main2.py --train False --model_type transformer
   ```

## Future Work

- Extend feature extraction to include time-frequency representations.
- Implement additional deep learning architectures (e.g., LSTMs, CNNs).
- Incorporate real-time HFO detection for clinical applications.

## Acknowledgments

This project is part of ongoing research at the Intelligent User Interfaces Lab (IUI-LAB) and integrates methods for advanced EEG analysis and machine learning.
