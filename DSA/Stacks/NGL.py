from collections import deque
nums =  [1, 3, 2, 4]

n = len(nums)

ans = [-1] * n
dq = deque()

for i in range(0,n):

    x = nums[i]

    while dq and dq[-1] <= x:
        dq.pop()

    if dq:
        ans[i] = dq[-1]
    
    dq.append(x)

print(ans)


