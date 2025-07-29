import math
from collections import deque

class DGIM:
    def __init__(self, window_size):
        self.window_size = window_size
        self.buckets = deque()

    def _expire_old_buckets(self, current_time):
        while self.buckets and self.buckets[0][1] <= current_time - self.window_size:
            self.buckets.popleft()

    def add_bit(self, bit, timestamp):
        self._expire_old_buckets(timestamp)
        if bit == 1:
            self.buckets.append((1, timestamp))
            self._merge_buckets()

    def _merge_buckets(self):
        i = len(self.buckets) - 1
        while i > 1:
            if self.buckets[i][0] == self.buckets[i - 1][0] == self.buckets[i - 2][0]:
                self.buckets[i - 1] = (self.buckets[i - 1][0] * 2, self.buckets[i - 1][1])
                del self.buckets[i]
                i -= 1
            else:
                i -= 1

    def estimate_count(self):
        total = 0
        for i, (size, _) in enumerate(self.buckets):
            if i == 0:
                total += size // 2
            else:
                total += size
        return total
