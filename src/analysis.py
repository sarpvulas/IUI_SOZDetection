import numpy as np

def select_hfo_values_for_specific_percentiles(soz_channels, non_soz_channels, hfo_results, run_key):
    """
    For each segment, extract a single HFO value at specific percentiles
    for SOZ and non-SOZ channels.

    Returns
    -------
    all_segment_results : list of dict
        Each element has {"soz": [...], "non_soz": [...]}
    """
    all_segment_results = []
    run_data = hfo_results.get(run_key, {})

    if not run_data:
        print(f"No HFO data for {run_key}")
        return []

    # Assume #segments = length of the first channel's list
    first_channel = next(iter(run_data.keys()), None)
    if first_channel is None:
        return []

    num_segments = len(run_data[first_channel])
    percentiles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    for seg_idx in range(num_segments):
        seg_result = {"soz": [], "non_soz": []}

        # Gather all SOZ channel HFO counts in this segment
        soz_counts = []
        for ch in soz_channels:
            if ch in run_data:
                soz_counts.append(run_data[ch][seg_idx])

        # Gather all non-SOZ channel HFO counts in this segment
        non_soz_counts = []
        for ch in non_soz_channels:
            if ch in run_data:
                non_soz_counts.append(run_data[ch][seg_idx])

        # Fallback if none collected
        if not soz_counts:
            soz_counts = [0]
        if not non_soz_counts:
            non_soz_counts = [0]

        soz_sorted = sorted(soz_counts)
        non_soz_sorted = sorted(non_soz_counts)

        # For each percentile p, pick the first value >= that percentile
        for p in percentiles:
            soz_thr = np.percentile(soz_sorted, p)
            non_soz_thr = np.percentile(non_soz_sorted, p)

            val_soz = next((v for v in soz_sorted if v >= soz_thr), 0)
            val_non_soz = next((v for v in non_soz_sorted if v >= non_soz_thr), 0)

            seg_result["soz"].append(val_soz)
            seg_result["non_soz"].append(val_non_soz)

        all_segment_results.append(seg_result)

    return all_segment_results


def write_hfo_values_to_py(all_segment_results, subject, run, output_file="hfo_data.py"):
    """
    Append the new SOZ/Non-SOZ percentiles to hfo_data in output_file.

    Structure:
    hfo_data = {
       "sub-jh101": {
          "01": {
             "SOZ Percentiles": [...],
             "Non-SOZ Percentiles": [...]
          }
       }
    }
    """
    new_data = {
        subject: {
            run: {
                'SOZ Percentiles': [seg["soz"] for seg in all_segment_results],
                'Non-SOZ Percentiles': [seg["non_soz"] for seg in all_segment_results]
            }
        }
    }

    try:
        with open(output_file, "r") as f:
            file_content = f.read()
            if "hfo_data =" in file_content:
                # CAUTION: In production, eval() can be dangerous.
                # A safer approach is to use ast.literal_eval or json
                hfo_data = eval(file_content.split("hfo_data =")[1].strip())
            else:
                hfo_data = {}
    except FileNotFoundError:
        hfo_data = {}

    # Merge new_data
    if subject in hfo_data:
        hfo_data[subject].update(new_data[subject])
    else:
        hfo_data.update(new_data)

    with open(output_file, "w") as f:
        f.write(f"hfo_data = {hfo_data}\n")

    print(f"Wrote data for {subject} run {run} to {output_file}")
