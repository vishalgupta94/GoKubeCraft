import heapq


print("baiscs of heaps")


li = [25, 20, 15, 30, 40]

heapq.heapify(li)
print("heap li",li)

heapq.heappush(li, 5)
print("min elemengt",heapq.heappop(li))