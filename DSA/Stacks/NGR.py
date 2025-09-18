from collections import deque
nums =  [1, 3, 2, 4]


ans = deque()
dq = deque()
for i in reversed(nums):
    print(i)

    while len(dq) and dq[-1] < i:
        dq.pop()

    if len(dq) == 0 :
        ans.appendleft(-1)
    else:
        ans.appendleft(dq[-1])
    
    dq.append(i)
print(list(ans))