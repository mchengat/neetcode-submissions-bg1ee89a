class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        currMax, currMin = 0, 0
        total = 0

        for num in nums:
            currMax = max(currMax+num, num)
            currMin = min(currMin+num, num)
            total += num
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)

        return max(globalMax, total - globalMin) if globalMax>0 else globalMax
