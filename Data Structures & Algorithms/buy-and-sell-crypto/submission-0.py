class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp = 0, 1
        maxP = 0

        while rp < len(prices):
            if prices[lp] < prices[rp]:
                profit = prices[rp] - prices[lp]
                maxP = max(profit, maxP)
            else:
                lp = rp
            rp +=1
        return maxP