from collections import defaultdict
s = "ababbc" 
k = 2

print("Longest substring with k unique character")

i, j, n, ans, freq = 0, 0, len(s), 0, defaultdict(int)

while j < n:
    
    freq[s[j]] += 1
    
    # print("frq",j,freq)
    if len(freq) < k:
        j+=1
        continue
    elif len(freq) == k:
        # print("Ans",s[i:j],i, j ,j - i + 1)
        ans = max(ans, j - i + 1)
        j+=1
    else:

        while len(freq) > k:
            freq[s[i]] -= 1

            if freq[s[i]] == 0:
                del freq[s[i]]
            i+=1
        j+=1    
        # print("extrs", freq)
print("Ans",ans)
# https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/1765826277/