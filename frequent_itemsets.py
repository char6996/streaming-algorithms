from collections import defaultdict

def extract_frequent_itemsets(sessions, min_support=2):
    item_count = defaultdict(int)

    for session in sessions:
        unique_items = set(session)
        for item in unique_items:
            item_count[item] += 1

    return {item: count for item, count in item_count.items() if count >= min_support}
