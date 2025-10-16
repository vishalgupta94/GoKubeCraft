from collections import defaultdict
s = "cbaebabacd"
p = "abc"

i, j, n, k, freq = 0, 0, len(s), len(p), defaultdict(int)
ans = []
for c in p:
    freq[c] += 1

while j < n:
    freq[s[j]] -= 1
    if freq[s[j]] == 0:
        del freq[s[j]]

    if j - i + 1 < k:
        j += 1
    else:
        if len(freq) == 0:
            ans.append(i)

        freq[s[i]] += 1
        if freq[s[i]] == 0:
            del freq[s[i]]            

        i += 1
        j += 1    

print("answer", ans)