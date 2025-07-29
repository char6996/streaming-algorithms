import matplotlib.pyplot as plt

def plot_frequency_bar_chart(frequencies, title="Top Frequent Items", top_n=10, filename="frequent_items.png"):
    """
    Plot a bar chart of top-N frequent items.
    """
    if not frequencies:
        print(f"[INFO] Skipping plot '{filename}' – no data to plot.")
        return

    # Sort and take top-N
    sorted_items = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:top_n]
    if not sorted_items:
        print(f"[INFO] No top items to plot for '{filename}'.")
        return

    items, counts = zip(*sorted_items)

    plt.figure(figsize=(10, 6))
    plt.bar(items, counts, color='skyblue')
    plt.title(title)
    plt.xlabel("Item ID")
    plt.ylabel("Estimated Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"[INFO] Saved plot: {filename}")


def plot_frequency_comparison(fixed_counts, decayed_counts, filename="comparison_plot.png"):
    """
    Compare fixed window and decayed window counts in a grouped bar chart.
    Uses union of item IDs to allow partial overlap.
    """
    all_items = set(fixed_counts.keys()) | set(decayed_counts.keys())
    if not all_items:
        print(f"[INFO] Skipping comparison plot – no items to plot.")
        return

    # Sort and take top-10 based on combined frequency (optional strategy)
    combined_counts = {item: fixed_counts.get(item, 0) + decayed_counts.get(item, 0) for item in all_items}
    top_items = sorted(combined_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    items = [item for item, _ in top_items]

    fixed_values = [fixed_counts.get(i, 0) for i in items]
    decayed_values = [decayed_counts.get(i, 0) for i in items]

    x = range(len(items))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar(x, fixed_values, width, label='Fixed Window')
    plt.bar([p + width for p in x], decayed_values, width, label='Decayed Window')

    plt.xlabel('Item ID')
    plt.ylabel('Count')
    plt.title('Comparison of Frequent Items (Top 10)')
    plt.xticks([p + width / 2 for p in x], items, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"[INFO] Saved comparison plot: {filename}")
