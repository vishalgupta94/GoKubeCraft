print("knapsack recursive")

weights_list = [2, 3, 4, 5, 9, 7, 3, 6, 8, 4]
values_list = [3, 4, 8, 8, 10, 7, 5, 9, 11, 6]
KNAPSACK_CAPACITY = 20


def recursive_knapsack(weights, values, capacity, index) -> int:
    if index == 0 or capacity == 0:
        return 0
    if weights[index - 1] <= capacity:
        return max(
            values[index - 1]
            + recursive_knapsack(
                weights, values, capacity - weights[index - 1], index - 1
            ),
            recursive_knapsack(weights, values, capacity, index - 1),
        )
    return recursive_knapsack(weights, values, capacity, index - 1)


print(
    recursive_knapsack(weights_list, values_list, KNAPSACK_CAPACITY, len(weights_list))
)


def dynamic_programming_knapsack(weights, values, KNAPSACK_CAPACITY, index) -> int:
    dp = [
        [0 for _ in range(KNAPSACK_CAPACITY + 1)] for _ in range(len(weights_list) + 1)
    ]

    for index in range(len(weights_list) + 1):
        for capacity in range(KNAPSACK_CAPACITY + 1):
            if index == 0 or capacity == 0:
                dp[index][capacity] = 0
            elif weights[index - 1] <= capacity:
                dp[index][capacity] = max(
                    dp[index - 1][capacity],
                    values[index - 1] + dp[index - 1][capacity - weights[index - 1]],
                )
            else:
                dp[index][capacity] = dp[index - 1][capacity]

    return dp[len(weights_list)][KNAPSACK_CAPACITY]


print(
    "knapsack dynamic programming",
    dynamic_programming_knapsack(
        weights_list, values_list, KNAPSACK_CAPACITY, len(weights_list)
    ),
)
