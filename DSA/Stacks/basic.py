from collections import deque

dq = deque()


dq.append(1)

dq.append(2)


print(dq[-1])  # 2

print(dq.pop()) # 2

print(dq.pop()) # 1

dq.appendleft(0)

print(dq[-1])  # 0

print(dq.pop()) # 0