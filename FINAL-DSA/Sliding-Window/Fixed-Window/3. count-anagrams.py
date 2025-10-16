# Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

# Example 1:

# Input: txt = "forxxorfxdofr", pat = "for"
# Output: 3
# Explanation: for, orf and ofr appears in the txt, hence answer is 3.

# Example 2:

# Input: txt = "aabaabaa", pat = "aaba"
# Output: 4
# Explanation: aaba is present 4 times in txt.

from collections import defaultdict

txt, pat = "aabaabaa", "aaba"

s, t = txt, pat


i, j, n, k, counter, freq = 0, 0, len(s), len(t), 0, defaultdict(int)

for character in t:
    freq[character] += 1

while j < n:
    freq[s[j]] -= 1

    if freq[s[j]] == 0:
        del freq[s[j]]

    if j - i + 1 < k:
        j +=1
    else:

        if not freq:
            counter += 1

        freq[s[i]] += 1    

        if freq[s[i]] == 0:
            del freq[s[i]]        

        j += 1
        i += 1    

print("counter",counter)