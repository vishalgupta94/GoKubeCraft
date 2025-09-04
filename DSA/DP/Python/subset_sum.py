arr = [1,2,5]
target_sum = 15


def recursive_subset_sum(arr, target_sum, index):
    if target_sum == 0:
        return True
    elif index == 0:
        return False
    elif arr[index - 1] <= target_sum:
        return recursive_subset_sum(
            arr, target_sum - arr[index - 1], index - 1
        ) or recursive_subset_sum(arr, target_sum, index - 1)
    else:
        return recursive_subset_sum(arr, target_sum, index - 1)


print("recursicve subset sum", recursive_subset_sum(arr, target_sum, len(arr)))


def dp_subset_sum(arr, target_sum, index):
    dp = [[False for _ in range(target_sum + 1)] for _ in range(len(arr) + 1)]

    for index in range(len(arr) + 1):
        for capacity in range(target_sum + 1):
            if capacity == 0:
                dp[index][capacity] = True
            elif index == 0:
                dp[index][capacity] = False
            elif capacity >= arr[index - 1]:
                dp[index][capacity] = (
                    dp[index - 1][capacity - arr[index - 1]] or dp[index - 1][capacity]
                )
            else:
                dp[index][capacity] = dp[index - 1][capacity]



print("dp subset sum", dp_subset_sum(arr, target_sum, 0))


def canPartition(nums) -> bool:
    sum_of_list = sum(nums)

    if sum_of_list % 2 != 0 :
        return False

    target_sum = sum_of_list // 2 
    
    dp = [ [False] * (target_sum + 1 ) for _ in range(len(nums) + 1) ]
    
    for index in range(0, len(nums) + 1):
        for capacity in range(target_sum + 1):
            if capacity == 0:
                dp[index][capacity] = True
            elif index == 0:
                dp[index][capacity] = False                    
            elif capacity >= nums[index - 1]:
                dp[index][capacity] = dp[index - 1][capacity] or dp[index-1][capacity - nums[index - 1]]
            else:
                dp[index][capacity] = dp[index - 1][capacity]

    for row in dp:
        print(row)
        
    return dp[len(nums)][target_sum]
                    

              

print("canPartition", canPartition(arr))    