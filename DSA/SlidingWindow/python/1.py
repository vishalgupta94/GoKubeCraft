d = dict()
arr = [1, 2, 3, 4, 5, 6, 7, 8]
for i in arr:
    d[i] = 1

print("d", d)
print("length", len(d))
del d[1]
print("delete ", len(d))
