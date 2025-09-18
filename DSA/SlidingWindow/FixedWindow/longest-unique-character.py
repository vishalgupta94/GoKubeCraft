from collections import defaultdict
s = "pwwkew"


print("Long substring with unique character")

i, j, n, freq, ans = 0, 0, len(s), defaultdict(int), 1


while j < n:
    freq[s[j]] += 1
   
    print(j, freq, ans)

    if j - i + 1 == len(freq):
        print("ans", s[i: j + 1])
        ans = max(ans, j - i + 1)
    elif j - i + 1 >  len(freq):
        
        while j - i + 1 >  len(freq):
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                del freq[s[i]]
            i += 1
    
    
    j += 1
            
print(ans)