s = "aabaacdaa"


dp = [ [-1 for _ in range(len(s))] for _ in range(len(s))]

def isPalindron(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True  

# print(isPalindron("aab"))
    
def solve(s, i, j):
    # print(dp[i][j])

    
    if i==j:
        print("2",s) 
        dp[i][j] = 0
        return 0 
    if isPalindron(s,i,j):
        dp[i][j] = 0
        return 0
    if dp[i][j] != -1:
        print("1",s, dp[i][j],i,j) 
        return dp[i][j]    
    else:
        print("3",s) 
        value = 99999999
        for k in range(i, j):
            print("31",s,i,k,j) 
            temp = solve(s, i, k) + solve(s, k + 1, j) + 1 
            value = min(value, temp)
            
            
        dp[i][j] = value
        return dp[i][j]    

solve(s,0,len(s)-1)
for row in dp:
    print(row)        