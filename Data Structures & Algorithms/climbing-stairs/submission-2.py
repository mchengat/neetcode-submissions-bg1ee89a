class Solution:
    def climbStairs(self, n: int) -> int:
        val, next = 0, 1
        while n > 0:
            val, next = next, val + next
            n -= 1
        return next