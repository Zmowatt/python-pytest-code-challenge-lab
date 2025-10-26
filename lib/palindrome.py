def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    n = len(s)
    if n < 2:
        return s
    start = 0
    max_len = 1
    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    for i in range(n):
        a = expand(i, i)
        b = expand(i, i + 1)
        best = max(a, b)
        if best > max_len:
            max_len = best
            start = i - (max_len - 1) // 2
    return s[start:start + max_len]