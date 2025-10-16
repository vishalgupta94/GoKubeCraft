# Example 1:

# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

# Example 2:

# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

# Example 3:

# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def find_last_negavtive(arr):
            low, high = 0, len(arr) - 1
            index = -1
            while low <= high:
                mid = (low + high ) //2

                if arr[mid] < 0:
                    index = mid
                    low = mid + 1 
                else:    
                    high = mid -1 
            return index

        def find_first_positive(arr):  
            low, high = 0, len(arr) - 1
            index = -1
            while low <= high:
                mid = (low + high ) //2

                if arr[mid] > 0:
                    index = mid
                    high = mid - 1 
                else:    
                    low = mid + 1 
            return index       

        last_negavtive = find_last_negavtive(nums)
        first_positive = find_first_positive(nums)

        print(last_negavtive,first_positive)

        if last_negavtive == -1 and  first_positive == -1:
            return 0 
        elif  last_negavtive == -1:
            return len(nums) - first_positive        
        elif  first_positive == -1:
            return last_negavtive + 1
        else:
             return max(last_negavtive + 1, len(nums) - first_positive   )       


# if last_negavtive == -1 and  first_positive == -1:
#     return 0 
# elif  last_negavtive == -1:
#     return len(arr) - first_positive        
# elif  first_positive == -1:
#     return last_negavtive      