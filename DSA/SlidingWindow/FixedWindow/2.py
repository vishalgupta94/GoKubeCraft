nums = [12, -1, -7, 8, 15, 30, 16, -28]
k = 3

i, j, n = 0, 0, len(nums)

ans = []

temp_ans = []

while j < n:
    if nums[j] < 0:
        temp_ans.append(nums[j])
        

    if j - i + 1 < k:
        j += 1
    else:
        
        if len(temp_ans) > 0:
            ans.append(temp_ans[0])
        else:
            ans.append(0)

        if nums[i] < 0 and temp_ans[0] == nums[i]:
            temp_ans.pop(0)

        i += 1
        j += 1    
print(ans)        