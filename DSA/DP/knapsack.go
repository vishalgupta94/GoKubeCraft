package main

import "fmt"

func main() {
	row, column := 5, 11

	var dp [][]int
	for i := range row {
		dp = append(dp, []int{})
		for j := range column {
			dp[i] = append(dp[i], j)
		}
	}
	fmt.Println("hello world", dp)
}

// func knapsack(w int, profit []int, weight []int) {
// 	length := len(weight)
// 	dp := make([][]int, length+1)

// 	for i := range length {
// 		dp[i] = make([]int, length)
// 	}

// 	fmt.Println("dp", dp)
// }

// func main() {
// 	w := 4
// 	profit := []int{1, 2, 3}
// 	weight := []int{4, 5, 1}

// 	fmt.Println("hello world", w, profit, weight)
// 	knapsack(w, profit, weight)
// }
