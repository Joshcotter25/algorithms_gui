def count_pal_substrings(s: str) -> int:
    n = len(s)
    memo = {}  # (i, j) -> bool

    def is_pal(i: int, j: int) -> bool:
        if i >= j:
            return True
        key = (i, j)
        if key in memo:
            return memo[key]
        memo[key] = (s[i] == s[j]) and is_pal(i + 1, j - 1)
        return memo[key]

    count = 0
    for i in range(n):
        for j in range(i, n):
            if is_pal(i, j):
                count += 1
    return count