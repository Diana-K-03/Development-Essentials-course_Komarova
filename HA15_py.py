def best_rod_cutting(prices, n):
    """
    prices: list where prices[i-1] is price for length i
    n: total rod length (int)
    Returns: (max_value, pieces)
    """
    if n <= 0:
        return 0, []
    dp = [float('-inf')] * (n + 1)
    dp[0] = 0
    cut = [0] * (n + 1)

    def piece_price(L):
        return prices[L - 1] if 1 <= L <= len(prices) else float('-inf')

    for i in range(1, n + 1):
        # consider selling whole piece if price known
        best = piece_price(i)
        first = 0 if best != float('-inf') else -1
        # try splitting into j and i-j
        for j in range(1, i):
            left = dp[j]
            right = dp[i - j]
            total = left + right
            if total > best:
                best = total
                first = j
        dp[i] = best
        cut[i] = first if first != -1 else i  # if nothing valid, fallback to whole length

    # reconstruct parts
    pieces = []
    length = n
    while length > 0:
        c = cut[length]
        if c == 0:
            pieces.append(length)
            break
        pieces.append(c)
        length -= c

    return int(dp[n]), pieces
