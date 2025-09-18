from collections import defaultdict
s = "ABAB"

k = 2


i, j, n , freq, ans = 0, 0, len(s), defaultdict(int), 0


while j < n:
    
    freq[s[j]] += 1
    print(freq)
    if len(freq) < 2:
        ans = max(ans, j - i + 1)
    elif len(freq) == 2:
        minVal = n
        for keys in freq.keys():
            minVal = min(minVal, freq[keys])
        
        if minVal <= k:
            ans = max(ans, j - i + 1)



    else:
        while len(freq) > 2:
            freq[s[i]] -= 1

            if freq[s[i]] == 0:
                del freq[s[i]]  
            i += 1          
    j +=1
print(ans)    