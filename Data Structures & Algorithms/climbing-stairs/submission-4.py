class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        
        if n == 2:
            return 2
        
        n1 , n2 = 1, 1
        for i in range(2, n+1):
            n1, n2 = n2, n1+n2
        return n2