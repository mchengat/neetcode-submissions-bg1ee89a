class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = 0
        currentOnes = 0
        for i in nums:
            if i == 1:
                currentOnes+=1
            else:
                maxNum = max(maxNum, currentOnes)
                currentOnes =0
        return max(maxNum, currentOnes)