from collections import deque
print("maximum area of histogram")
heights = [2,1,5,6,2,3]

nsrList = []
nslList = []

dq = deque()

for i in range(len(heights)):
    x = heights[i]

    while dq and dq[-1][0] >= x:
        dq.pop()

    if dq:
        nslList.append(i - dq[-1][1] -1 )
    else:
        nslList.append(i)

    dq.append((x,i))    

dq = deque()

for i in range(len(heights) - 1, -1, - 1):
    x = heights[i]

    while dq and dq[-1][0] >= x:
        dq.pop()

    if dq:
        nsrList.append(dq[-1][1] - 1 - i)
    else:
        nsrList.append(len(heights) - 1 - i)

    dq.append((x,i))    


print("0nslList",nslList)
print("nsrList",nsrList[::-1])

maxArea = 0 
for i in range(len(heights)):
    x = heights[i]

    maxArea = max(maxArea, x * (nslList[i] + nsrList[::-1][i] + 1) )

print("maxArea",maxArea)