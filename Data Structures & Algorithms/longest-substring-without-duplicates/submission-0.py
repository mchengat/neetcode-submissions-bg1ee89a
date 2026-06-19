class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        unique_chars = {}
        res = 0
        for R in range(len(s)):
            if s[R] in unique_chars:
                L = max(L, unique_chars[s[R]] + 1)
            unique_chars[s[R]] = R
            res = max(res, R-L +1)
        return res
