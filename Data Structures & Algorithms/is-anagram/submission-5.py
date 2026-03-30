class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        result = {}
        for char in s:
            if char in result:
                result[char] += 1
            else:
                result[char] = 1

        for char in t:
            if char not in result or result.get(char) == 0:
                return False
            result[char] -= 1
        return True
