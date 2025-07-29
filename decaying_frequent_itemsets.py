import time
from collections import defaultdict
from math import exp

class DecayingFrequencyCounter:
    def __init__(self, decay_rate=0.01):
        self.item_counts = defaultdict(float)
        self.last_updated = {}
        self.decay_rate = decay_rate

    def _apply_decay(self, item, current_time):
        if item in self.last_updated:
            elapsed = current_time - self.last_updated[item]
            self.item_counts[item] *= exp(-self.decay_rate * elapsed)
        self.last_updated[item] = current_time

    def add(self, item, timestamp):
        self._apply_decay(item, timestamp)
        self.item_counts[item] += 1.0

    def get_top_items(self, k=10):
        return sorted(self.item_counts.items(), key=lambda x: x[1], reverse=True)[:k]

    def get_all_counts(self):
        return dict(self.item_counts)
