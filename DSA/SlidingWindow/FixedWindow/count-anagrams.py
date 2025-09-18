from collections import defaultdict
s = "aabaabaa" 
p = "aaba"

print("Longest substring with k unique character")

i, j, n, k, freq, ans  = 0, 0, len(s), len(p), defaultdict(int), []

for ch in p:
    freq[ch] += 1

while j < n:
    # print(j, freq)
    freq[s[j]] -= 1
    if freq[s[j]] == 0:
        del freq[s[j]]

    if j - i + 1 < k:
        j += 1
    else:

        if len(freq) == 0:
            # print("answer", i, j, s[i:j+1])
            ans.append(i)

        freq[s[i]] += 1
        if freq[s[i]] == 0:
           del freq[s[i]]
        i += 1
        j += 1    

print(ans)


# https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/1765826277/