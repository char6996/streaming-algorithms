from data_loader import load_events
from stream_miner import StreamFrequentMiner
from stream_simulator import simulate_stream
from decaying_frequent_itemsets import DecayingFrequencyCounter
from plot_utils import plot_frequency_bar_chart, plot_frequency_comparison

def run_fixed_window_frequent_items():
    print("=== Fixed Window Frequent Items ===")
    events_df = load_events("events.csv")
    miner = StreamFrequentMiner(window_size=3600)  # 1 hour window

    for _, row in events_df.iterrows():
        timestamp = row['timestamp']
        item_id = row['item_id']
        miner.process_event(timestamp, item_id)

    frequencies = miner.estimate_frequencies()
    top_items = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:10]

    print("Top frequent items in the stream (fixed window):")
    for item, count in top_items:
        print(f"Item ID: {item}, Estimated Count: {count}")

    plot_frequency_bar_chart(dict(top_items), title="Top Frequent Items (Fixed Window)", filename="fixed_window_plot.png")
    return dict(top_items)

def run_decaying_window_frequent_items():
    print("\n=== Time-Decaying Window Frequent Items ===")
    decay_counter = DecayingFrequencyCounter(decay_rate=0.00005)

    for event in simulate_stream("events.csv"):
        item_id = event.get("item_id")
        timestamp = event.get("timestamp")
        if item_id:
            decay_counter.add(item_id, timestamp)

    frequencies = decay_counter.get_all_counts()
    top_items = decay_counter.get_top_items(10)

    print("Top frequent items in the stream (decaying window):")
    for item, count in top_items:
        print(f"Item ID: {item}, Decayed Count: {count:.2f}")

    plot_frequency_bar_chart(dict(top_items), title="Top Frequent Items (Decaying Window)", filename="decaying_window_plot.png")
    return dict(top_items)

def main():
    fixed_counts = run_fixed_window_frequent_items()
    decayed_counts = run_decaying_window_frequent_items()
    plot_frequency_comparison(fixed_counts, decayed_counts, filename="comparison_plot.png")

if __name__ == "__main__":
    main()
