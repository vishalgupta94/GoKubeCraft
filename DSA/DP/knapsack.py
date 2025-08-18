from typing import List


W = 10
profit = [4, 5, 10, 11, 13]
weight = [3, 4, 7, 8, 9]

dp = [ [0 for _ in range(W+1)] for _ in range(len(weight)+1) ]
print(dp)

for row in range(1, len(weight)+1):
    for col in range(1, W+1):
        if row == 0 or col == 0:
            dp[row][col] = 0 
        elif weight[row-1] > col:
            dp[row][col] = dp[row-1][col]
        else:
            dp[row][col] = max(dp[row-1][col],profit[row-1]+ dp[row-1][col-weight[row-1]])  
for x in dp:
    print(x)         
"""
from typing import List

def knapsack(w: int, profit: List[int], weight: List[int] ) -> None :
    dp =  [ [0 for _ in range(w+1)] for _ in range(len(weight))]
    print("dp",dp)
    
W,profit,weight = 4,[1, 2, 3],[4, 5, 1]
knapsack(W, profit, weight)
"""
