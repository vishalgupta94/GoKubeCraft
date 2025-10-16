# Given an array arr[] of integers and an integer k, your task is to find the maximum value for each contiguous subarray of size k.
# Output : maximum window sum

arr, k = [1, 2, 3, 1, 4, 5, 2, 3, 6], 3


i, j, n, window_sum, max_sum = 0, 0, len(arr), 0, float("-inf")

while j < n:
    window_sum += arr[j]

    if j - i + 1 < k:
        j += 1
    else:
        # window size == k
        max_sum = max(max_sum, window_sum)
        window_sum -= arr[i]
        i += 1
        j += 1

print("Maximum window sum", max_sum)
