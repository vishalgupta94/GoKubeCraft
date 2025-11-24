def findPages( nums, m):

    if m > len(nums):
        return -1
    
    low, high = max(nums), sum(nums)

    def checkForAns(tempAns):
        index, current = 1, 0
        for i in nums:
            
            current += i
            print("index, current",index, current,tempAns)
            if current > tempAns:
                index += 1
                current = i
        print("final index",index)
        return index <= m
    
    actualAns = -1
    while low <= high:

        mid = (low+ high) //2
        print("mid",mid,low, high)
        # //try to fit low into solution
        tempAns = checkForAns(mid)
        print("Temp4",tempAns)
        if tempAns:
            actualAns = mid;
            high = mid - 1                 
        else:
            low = mid + 1       


    return actualAns

print(findPages([13 ,31 ,37, 45, 46, 54 ,55 ,63 ,73, 84, 85], 9))   

# print(findPages([12, 34, 67, 90], 2))   