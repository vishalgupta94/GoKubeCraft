def aggressiveCows( stalls, k):
    # code here
    
    stalls.sort()

        
    low, high = 1, stalls[-1] - stalls[0]

        
    
    def check(distance):
        placed = 1 
        lastCow = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - lastCow >= distance:
                lastCow = stalls[i]
                placed += 1
        return placed >= k        
    
    ans = -1    
    while low <= high:
        mid = (low + high) //2
        # print("oldmid",mid)
        
        # // try to fit cow at mid distance between one another
        if check(mid) == True:
            ans = mid 
            # print("answer found",ans)
            low = mid + 1
        else:
            high = mid - 1
    
    return ans

print(aggressiveCows([10, 1, 2, 7, 5], 3))