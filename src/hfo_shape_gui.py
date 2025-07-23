# src/hfo_shape_gui.py

import os
import pickle
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class HFOViewer(tk.Tk):
    """
    A simple GUI to browse HFO waveform snippets by patient, run, channel, and event.
    Loads 'src/hfo_shape_results.pkl' (produced by extract_hfo_waveforms_in_segments)
    and displays each event's raw-EEG waveform when selected.
    """

    def __init__(self, pickle_path="src/hfo_shape_results.pkl"):
        super().__init__()
        self.title("HFO Event Viewer")
        self.geometry("1000x600")

        # Load pickle file
        if not os.path.exists(pickle_path):
            messagebox.showerror("Error", f"Pickle file not found: {pickle_path}")
            self.destroy()
            return

        with open(pickle_path, "rb") as f:
            self.hfo_shape_results = pickle.load(f)

        # Parse available patients and runs from run_keys (e.g., "sub-jh101_01")
        self.run_keys = list(self.hfo_shape_results.keys())
        self.subjects = sorted({rk.split("_", 1)[0] for rk in self.run_keys})

        # GUI Variables
        self.selected_subject = tk.StringVar()
        self.selected_run = tk.StringVar()
        self.selected_channel = tk.StringVar()

        # Build GUI components
        self._build_controls()
        self._build_plot_area()

        # Initially populate subject dropdown
        self.subject_combo["values"] = self.subjects
        if self.subjects:
            self.subject_combo.current(0)
            self._on_subject_change()

    def _build_controls(self):
        control_frame = tk.Frame(self)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Subject dropdown
        tk.Label(control_frame, text="Patient (Subject):").grid(row=0, column=0, sticky="w")
        self.subject_combo = ttk.Combobox(
            control_frame, textvariable=self.selected_subject, state="readonly"
        )
        self.subject_combo.grid(row=0, column=1, padx=5, sticky="w")
        self.subject_combo.bind("<<ComboboxSelected>>", lambda _: self._on_subject_change())

        # Run dropdown
        tk.Label(control_frame, text="Run:").grid(row=0, column=2, sticky="w", padx=(20, 0))
        self.run_combo = ttk.Combobox(
            control_frame, textvariable=self.selected_run, state="readonly"
        )
        self.run_combo.grid(row=0, column=3, padx=5, sticky="w")
        self.run_combo.bind("<<ComboboxSelected>>", lambda _: self._on_run_change())

        # Channel dropdown
        tk.Label(control_frame, text="Channel:").grid(row=0, column=4, sticky="w", padx=(20, 0))
        self.channel_combo = ttk.Combobox(
            control_frame, textvariable=self.selected_channel, state="readonly", width=20
        )
        self.channel_combo.grid(row=0, column=5, padx=5, sticky="w")
        self.channel_combo.bind("<<ComboboxSelected>>", lambda _: self._on_channel_change())

        # Event listbox
        tk.Label(control_frame, text="Event Index:").grid(row=0, column=6, sticky="w", padx=(20, 0))
        self.event_listbox = tk.Listbox(control_frame, height=5, exportselection=False)
        self.event_listbox.grid(row=0, column=7, padx=5, sticky="w")
        self.event_listbox.bind("<<ListboxSelect>>", lambda _: self._on_event_select())

    def _build_plot_area(self):
        # Frame for plotting
        plot_frame = tk.Frame(self)
        plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        self.fig = Figure(figsize=(8, 5))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("HFO Waveform")
        self.ax.set_xlabel("Sample Index")
        self.ax.set_ylabel("Amplitude (μV)")

        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _on_subject_change(self):
        # Update runs dropdown based on selected subject
        subject = self.selected_subject.get()
        runs = sorted(
            rk.split("_", 1)[1]
            for rk in self.run_keys
            if rk.split("_", 1)[0] == subject
        )
        self.run_combo["values"] = runs
        if runs:
            self.run_combo.current(0)
            self._on_run_change()
        else:
            self.run_combo["values"] = []
            self.channel_combo["values"] = []
            self.event_listbox.delete(0, tk.END)
            self._clear_plot()

    def _on_run_change(self):
        # Update channels dropdown based on selected (subject, run)
        subject = self.selected_subject.get()
        run = self.selected_run.get()
        run_key = f"{subject}_{run.zfill(2)}" if len(run) == 1 else f"{subject}_{run}"
        if run_key not in self.hfo_shape_results:
            self.channel_combo["values"] = []
            self.event_listbox.delete(0, tk.END)
            self._clear_plot()
            return

        channels = sorted(self.hfo_shape_results[run_key].keys())
        self.channel_combo["values"] = channels
        if channels:
            self.channel_combo.current(0)
            self._on_channel_change()
        else:
            self.event_listbox.delete(0, tk.END)
            self._clear_plot()

    def _on_channel_change(self):
        # Update event list based on selected (subject, run, channel)
        subject = self.selected_subject.get()
        run = self.selected_run.get()
        run_key = f"{subject}_{run.zfill(2)}" if len(run) == 1 else f"{subject}_{run}"
        channel = self.selected_channel.get()

        self.event_listbox.delete(0, tk.END)
        self._clear_plot()

        if not run_key or not channel or run_key not in self.hfo_shape_results:
            return

        segments_dict = self.hfo_shape_results[run_key].get(channel, {})
        # Flatten events: (segment_id, event_idx) pairs
        self.event_index_map = []
        for seg_id, events in sorted(segments_dict.items()):
            for ev_idx, _ in enumerate(events):
                display_label = f"Seg {seg_id}, Ev {ev_idx}"
                self.event_listbox.insert(tk.END, display_label)
                self.event_index_map.append((seg_id, ev_idx))

        # If there is at least one event, select the first by default
        if self.event_index_map:
            self.event_listbox.selection_set(0)
            self._on_event_select()

    def _on_event_select(self):
        # Plot waveform for the selected event
        selection = self.event_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        seg_id, ev_idx = self.event_index_map[idx]

        subject = self.selected_subject.get()
        run = self.selected_run.get()
        run_key = f"{subject}_{run.zfill(2)}" if len(run) == 1 else f"{subject}_{run}"
        channel = self.selected_channel.get()

        event = self.hfo_shape_results[run_key][channel][seg_id][ev_idx]
        waveform = event["waveform"]
        # Compute midpoint of the snippet directly (since mid_sample is no longer stored)
        mid_index = len(waveform) // 2

        self._plot_waveform(waveform, mid_index)

    def _plot_waveform(self, waveform, mid_index):
        self.ax.clear()
        self.ax.plot(waveform, color="blue", linewidth=1.5)
        # Mark the center of the snippet
        self.ax.axvline(x=mid_index, color="red", linestyle="--", label="Midpoint")
        self.ax.set_title("HFO Waveform")
        self.ax.set_xlabel("Sample Index")
        self.ax.set_ylabel("Amplitude (μV)")
        self.ax.legend(loc="upper right")
        self.ax.grid(True)
        self.canvas.draw()

    def _clear_plot(self):
        self.ax.clear()
        self.ax.set_title("HFO Waveform")
        self.ax.set_xlabel("Sample Index")
        self.ax.set_ylabel("Amplitude (μV)")
        self.canvas.draw()


if __name__ == "__main__":
    # Launch the GUI, pointing to the correct pickle location
    app = HFOViewer(pickle_path="hfo_shape_results.pkl")
    app.mainloop()
