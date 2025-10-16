from typing import List
from collections import Counter
import heapq

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        h = []
        for i in freq:
            key, value = i, freq[i]
            # min-heap on (frequency asc, value desc) => use -key for tie-break
            heapq.heappush(h, (value, -key))

        ans = []
        while h:
            frequency, neg_key = heapq.heappop(h)
            key = -neg_key
            for _ in range(frequency):
                ans.append(key)

        return ans
