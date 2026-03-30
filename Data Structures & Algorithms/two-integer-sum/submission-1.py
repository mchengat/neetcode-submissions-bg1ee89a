class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dups = {}
        result = []
        for i, num in enumerate(nums):
            print(dups)
            curr = target - num
            if curr in dups:
                return [dups[curr], i]
            dups[num] = i

        return result