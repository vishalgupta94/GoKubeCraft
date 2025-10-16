from collections import deque
nums =  [4, 5, 2, 10, 8]

print("Next smallest left")

dq, ans = deque(), []
for i in nums:
  
    while dq and dq[-1] > i:
        dq.pop()

    if dq:
        ans.append(dq[-1])
    else:
        ans.append(-1)

    dq.append(i)    

print("ans",ans)