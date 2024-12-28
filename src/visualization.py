import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_hfo_heatmap(hfo_results, run_key='sub-jh101_01'):
    """
    Create a heatmap of HFO counts for a given run_key. Rows=channels, columns=segments.
    """
    run_data = hfo_results.get(run_key, {})
    if not run_data:
        print(f"No HFO data found for {run_key}")
        return

    channel_names = list(run_data.keys())
    if not channel_names:
        print(f"No channels found in {run_key}")
        return

    # Collect HFO counts
    heatmap_data = []
    for ch in channel_names:
        heatmap_data.append(run_data[ch])  # list of segment-wise counts

    # Convert to DataFrame
    df = pd.DataFrame(heatmap_data, index=channel_names)
    df.columns = [f"Segment {i+1}" for i in range(df.shape[1])]

    plt.figure(figsize=(12, 6))
    sns.heatmap(df, annot=False, cmap='coolwarm', cbar=True)
    plt.title(f'HFO Heatmap for {run_key}')
    plt.xlabel('Segments')
    plt.ylabel('Channels')
    plt.show()
