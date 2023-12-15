def print_all_common_subsequences(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print("Length:",dp[m][n])
    def backtrack(i, j, current_subsequence):
        if i == 0 or j == 0:
            print(current_subsequence[::])
            return
        if X[i - 1] == Y[j - 1]:
            backtrack(i - 1, j - 1, X[i - 1] + current_subsequence)
        elif dp[i - 1][j] > dp[i][j - 1]:
            backtrack(i - 1, j, current_subsequence)
        elif dp[i - 1][j] < dp[i][j - 1]:
            backtrack(i, j - 1, current_subsequence)
        else:
            backtrack(i - 1, j, current_subsequence)
            backtrack(i, j - 1, current_subsequence)
    backtrack(m, n, "")
X = input("ENter main String:")
Y = input("Enter Sub-string:")
print_all_common_subsequences(X, Y)
