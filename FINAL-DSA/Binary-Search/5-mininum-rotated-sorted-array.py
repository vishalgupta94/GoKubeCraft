# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

class Solution:
    def findMin(self, nums: List[int]) -> int:

        low, high = 0, len(nums) - 1
        min_value = 5001 
        while low <= high:
            mid = (low + high) //2

            if nums[low] <= nums[mid]:
                min_value = min(min_value, nums[low])
                low = mid + 1
            else:
                min_value = min(min_value, nums[mid])
                high = mid - 1
        return min_value       