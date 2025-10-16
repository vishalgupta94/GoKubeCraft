# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:

# Input: nums = [1], target = 0
# Output: -1

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_in_rotated_array(nums: List[int]) -> int:
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    return mid
                elif nums[low] <= nums[mid]:  # left side is sorted
                    if nums[low] <= target <= nums[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:  # right side is sorted
                    if nums[mid] <= target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1

            return -1  # ensure int is always returned

        ans = search_in_rotated_array(nums)
        return ans  # ans is guaranteed int now