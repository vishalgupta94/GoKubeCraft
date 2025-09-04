from collections import defaultdict

nums = [1, 5, 4, 2, 9, 9, 9]
k = 3

freq = defaultdict(int)
window_sum = 0
best = 0

i, j = 0, 0

while j < len(nums):
    x, y = nums[i], nums[j]

    freq[y] += 1

    window_sum += y

    if j - i + 1 < k:
        j += 1
    else:
        if len(freq) == k:
            best = max(best, window_sum)

        window_sum -= x
        freq[x] -= 1
        if freq[x] == 0:
            del freq[x]

        i += 1
        j += 1
print(best)
