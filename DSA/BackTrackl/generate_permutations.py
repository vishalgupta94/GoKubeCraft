from typing import List


class Solution:
    def generate_permutations(
        self, nums: List[int], start_index: int, last_index: int, ans: List[List[int]]
    ) -> None:
        if start_index == last_index - 1:
            ans.append(nums[:])
        else:
            for index in range(start_index, last_index):
                nums[start_index], nums[index] = nums[index], nums[start_index]
                self.generate_permutations(nums, start_index + 1, last_index, ans)
                nums[start_index], nums[index] = nums[index], nums[start_index]

    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: List[List[int]] = []
        self.generate_permutations(nums, 0, len(nums), permutations)
        return permutations


sol = Solution()
print(sol.permute([1, 2, 3]))
