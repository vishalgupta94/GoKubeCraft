package main1

import "fmt"

func gen_permutations(nums []int, startIndex int, permutations *[][]int) {
	if startIndex == len(nums)-1 {
		emptySlice := make([]int, len(nums))
		copy(emptySlice, nums)
		*permutations = append(*permutations, emptySlice)
		return
	} else {
		for i := startIndex; i < len(nums); i++ {
			nums[i], nums[startIndex] = nums[startIndex], nums[i]
			gen_permutations(nums, startIndex+1, permutations)
			nums[i], nums[startIndex] = nums[startIndex], nums[i]
		}
	}
}

func permute(nums []int) [][]int {
	var ans [][]int
	gen_permutations(nums, 0, &ans)
	return ans
}

func main() {
	nums := []int{1, 2, 3}
	fmt.Println("hello world")
	fmt.Println(permute(nums))
}
