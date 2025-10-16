# First Negative Number in every Window of Size K

# Input: arr[] = [12, -1, -7, 8, -15, 30, 16, 28] , k = 3
# Output: [-1, -1, -7, -15, -15, 0]

from collections import deque

arr, k = [12, -1, -7, 8, -15, 30, 16, 28], 3

i, j, n, dq, ans = 0, 0, len(arr), deque(), []

while j < n:
    if arr[j] < 0:
        dq.append(j)

    if j - i + 1 < k:
        j += 1
    else:

        if not dq:
            ans.append(0)
        else:
            ans.append(arr[dq[0]])

        if dq and dq[0] == i:
            dq.popleft()

        i += 1
        j += 1

print("ans", ans)



dq = deque()

# ----- Add elements -----
dq.append(10)       # append to right end → [10]
dq.appendleft(5)    # append to left end → [5, 10]

# ----- Remove elements -----
dq.pop()            # remove from right end → returns 10
dq.popleft()        # remove from left end → returns 5

# ----- Access elements -----
dq.append(1)
dq.append(2)
dq.append(3)
print(dq[0])        # top of left (front element) → 1
print(dq[-1])       # top of right (rear element) → 3

# ----- Other useful ops -----
len(dq)             # number of elements
dq.clear()          # remove all elements