import heapq
from typing import List
from collections import defaultdict

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h, ans = [], []

        for i in arr:
            if len(h) < k:
                heapq.heappush(h, (-1 * abs(i - x), -i))
            else:
                diff, val = h[0]
                newDiff = -diff
                curDiff = abs(i - x)
                
                # If current element is closer, or equally close but smaller
                if curDiff < newDiff or (curDiff == newDiff and i < -val):
                    heapq.heappushpop(h, (-curDiff, -i))
        
        while h:
            _, item = heapq.heappop(h)
            ans.append(-item)

        ans.sort()
        return ans
# https://leetcode.com/problems/find-k-closest-elements/