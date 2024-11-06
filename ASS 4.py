def knapsack_01(profit, weights, capacity):
    n = len(profit)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + profit[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1
    return dp[n][capacity], selected_items
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    profit = []
    weights = []
    for i in range(n):
        p = int(input(f"Enter profit for item {i + 1}: "))
        w = int(input(f"Enter weight for item {i + 1}: "))
        profit.append(p)
        weights.append(w)
    capacity = int(input("Enter the capacity of the knapsack: "))
    max_profit, selected_items = knapsack_01(profit, weights, capacity)
    print("Maximum Profit:", max_profit)
    print("Selected items:", selected_items)