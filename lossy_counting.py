from collections import defaultdict
import math

class LossyCounting:
    def __init__(self, epsilon):
        self.epsilon = epsilon
        self.N = 0
        self.bucket_width = math.ceil(1 / epsilon)
        self.buckets = defaultdict(lambda: [0, 0])

    def add(self, item):
        self.N += 1
        if item in self.buckets:
            self.buckets[item][0] += 1
        else:
            self.buckets[item] = [1, self.N // self.bucket_width - 1]

        if self.N % self.bucket_width == 0:
            self._trim()

    def _trim(self):
        to_delete = []
        for item, (count, delta) in self.buckets.items():
            if count + delta <= self.N // self.bucket_width:
                to_delete.append(item)
        for item in to_delete:
            del self.buckets[item]

    def get_frequent_items(self, support_threshold):
        return {item: count for item, (count, _) in self.buckets.items() if count >= support_threshold}
