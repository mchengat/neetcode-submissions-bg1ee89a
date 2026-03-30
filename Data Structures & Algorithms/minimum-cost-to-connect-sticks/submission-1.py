class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            min1 = heapq.heappop(sticks)
            min2 = heapq.heappop(sticks)
            combined = min1 + min2
            cost += combined
            heapq.heappush(sticks, combined)
        return cost