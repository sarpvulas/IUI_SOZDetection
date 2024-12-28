import numpy as np
import torch
from torch.utils.data import Dataset
from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


# -------------
# Dataset class
# -------------
class EEGDataset(Dataset):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __len__(self):
        return len(self.Y)

    def __getitem__(self, idx):
        # Convert each feature vector to float
        input_ids = torch.tensor(self.X[idx], dtype=torch.float)
        attention_mask = torch.ones_like(input_ids)  # trivial mask
        labels = torch.tensor(self.Y[idx], dtype=torch.long)
        return {
            "input_ids": input_ids.to(dtype=torch.long),
            "attention_mask": attention_mask,
            "labels": labels
        }


# -------------
# Metrics
# -------------
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)
    acc = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds)
    prec = precision_score(labels, preds)
    rec = recall_score(labels, preds)
    return {
        "accuracy": acc,
        "f1": f1,
        "precision": prec,
        "recall": rec
    }


# -------------
# Transformer
# -------------
def train_transformer(X, Y):
    dataset = EEGDataset(X, Y)
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="steps",
        eval_steps=50,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=30,
        logging_dir="./logs",
        logging_steps=10,
        save_steps=50,
        save_total_limit=2,
        load_best_model_at_end=True,
        metric_for_best_model="f1",
        report_to="none"
    )

    model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        eval_dataset=dataset,
        compute_metrics=compute_metrics
    )

    trainer.train()
    eval_results = trainer.evaluate()
    print("\nTransformer Evaluation Results:")
    for k, v in eval_results.items():
        print(f"  {k}: {v:.4f}")

    return model


# ------------------
# Random Forest
# ------------------
def train_random_forest(X, Y):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    rf = RandomForestClassifier(
        max_depth=10,
        max_features='sqrt',
        min_samples_split=10,
        n_estimators=50,
        random_state=42
    )
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    _print_metrics(y_test, y_pred, title="RandomForestClassifier")
    return rf


# ------------------
# CatBoost
# ------------------
def train_catboost(X, Y):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    cat_model = CatBoostClassifier(
        iterations=100,
        depth=6,
        learning_rate=0.001,
        random_seed=42,
        verbose=False
    )
    cat_model.fit(X_train, y_train)
    y_pred = cat_model.predict(X_test)
    _print_metrics(y_test, y_pred, title="CatBoostClassifier")
    return cat_model


# Helper to print classification metrics
def _print_metrics(y_test, y_pred, title="Model"):
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=["Class 0", "Class 1"])

    print(f"\nUsing {title}:")
    print(f"Accuracy: {acc:.2f}")
    print(f"F1 Score: {f1:.2f}")
    print("Confusion Matrix:")
    print(cm)
    print("Classification Report:")
    print(report)
