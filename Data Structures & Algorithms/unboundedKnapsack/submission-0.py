class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M = len(profit), capacity
        cache = [[-1] * (M+1) for _ in range(N)]
        return self.dfs(0, capacity, weight, profit, cache)

    def dfs(self, index, capacity, weight, profit, cache):
        if index == len(profit):
            return 0
        if cache[index][capacity] != -1:
            return cache[index][capacity]
        maxProfit = self.dfs(index+1, capacity, weight, profit, cache)
        newCap = capacity - weight[index]
        if newCap >= 0:
            p = profit[index] + self.dfs(index, newCap, weight, profit, cache)
            maxProfit = max(maxProfit, p)
        cache[index][capacity] = maxProfit
        return maxProfit