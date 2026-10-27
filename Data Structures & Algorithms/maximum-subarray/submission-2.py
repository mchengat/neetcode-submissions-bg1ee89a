class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        currSum = 0
        for i in range(len(nums)):
            currSum = max(currSum, 0)
            currSum += nums[i]
            maxSum = max(currSum,maxSum )
        return maxSum