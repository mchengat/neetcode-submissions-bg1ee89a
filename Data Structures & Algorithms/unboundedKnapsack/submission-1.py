class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)

        if capacity <=0 or len(weight) != n or n == 0:
            return 0

        dp = [[-1 for _ in range(capacity + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0

        for i in range(n):
            for c in range(1, capacity+1):
                profit1, profit2 = 0, 0
                if weight[i] <= c:
                    profit1 = profit[i] + dp[i][c-weight[i]]
                if i>0:
                    profit2 = dp[i-1][c]
                dp[i][c] = profit1 if profit1 > profit2 else profit2
            
        return dp[n-1][capacity]