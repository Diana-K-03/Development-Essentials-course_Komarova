import numpy as np

def best_rod_cutting(prices, n):
    dp = np.zeros(n + 1, dtype=int)
    cut = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = -1
        for j in range(1, i + 1):
            if max_val < prices[j - 1] + dp[i - j]:
                max_val = prices[j - 1] + dp[i - j]
                cut[i] = j
        dp[i] = max_val

    lengths = []
    while n > 0:
        lengths.append(cut[n])
        n -= cut[n]

    return dp[-1], lengths


prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
value, cuts = best_rod_cutting(prices, n)
print("Maximum Value:", value)
print("Recommended lengths:", cuts)