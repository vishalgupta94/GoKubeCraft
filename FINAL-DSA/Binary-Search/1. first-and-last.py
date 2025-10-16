# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# First and last occurrence of an element - LeetCode

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# nums, target = [5,7,7,8,8,10], 8
nums, target = [5, 7, 7, 8, 8, 10], 6


def lower_index_bs(arr, target):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            print("low", result)
            result = mid
            high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return result


def higher_index_bs(arr, target):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            print("high", result)
            result = mid
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return result


lower_index = lower_index_bs(nums, target)
higher_index = higher_index_bs(nums, target)

print([lower_index, higher_index])
