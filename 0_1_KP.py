n=int(input("Enter number of items: "))
weights=list(map(int,input("Enter the weights: ").split()))
values=list(map(int,input("Enter the profits: ").split()))
cap=int(input("Enter capacity: "))
dp = [[0] * (cap + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(1, cap + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
        else:
            dp[i][w] = dp[i - 1][w]
selected_items = []
i, w = n, cap
while i > 0 and w > 0:
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(i - 1)
        w -= weights[i - 1]
    i -= 1
print("Selected items: ",selected_items)
print("Maximum profit: ",dp[n][cap])
