from collections import defaultdict
from dgim import DGIM

class StreamFrequentMiner:
    def __init__(self, window_size):
        self.window_size = window_size
        self.item_trackers = defaultdict(lambda: DGIM(window_size))

    def process_event(self, event_time, item_id):
        self.item_trackers[item_id].add_bit(1, event_time.timestamp())

    def estimate_frequencies(self):
        return {item: tracker.estimate_count() for item, tracker in self.item_trackers.items()}
