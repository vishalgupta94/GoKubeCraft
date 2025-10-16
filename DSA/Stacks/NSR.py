from collections import deque
nums =  [4, 5, 2, 10, 8]

print("Next smallest right")

dq, ans = deque(), deque()
for i in reversed(nums):
    print(i,dq)
    while dq and dq[-1] > i:
        dq.pop()

    if dq:
        ans.appendleft(dq[-1])
    else:
        ans.appendleft(-1)

    dq.append(i)    

print("ans",list(ans))