nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

i, j = 0, 0
n = len(nums)

window_sum, best = 0, 0

while j < n:
    print(i, window_sum)
    window_sum += nums[j]

    if j - i + 1 < k:
        j += 1
    else:
        best = max(best, window_sum)
        window_sum -= nums[i]

        j += 1
        i += 1

print("best", best)
