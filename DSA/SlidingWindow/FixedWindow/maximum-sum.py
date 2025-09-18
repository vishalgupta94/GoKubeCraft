nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4


i, j, n = 0, 0, len(nums)

window_sum, best = 0, 0


while j < n:
    window_sum += nums[j]

    if j - i + 1 < k:
        j+=1
    else:
        best = max(best, window_sum)
        window_sum -= nums[i]        

        i+=1
        j+=1

print("windowSum",best)        
        