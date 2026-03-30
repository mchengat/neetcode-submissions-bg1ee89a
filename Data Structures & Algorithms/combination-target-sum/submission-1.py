class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current_combo, remaining):
            if remaining == 0:
                result.append(list(current_combo))
                return
            for i in range(start, len(nums)):
                candidate = nums[i]
                if candidate > remaining:
                    continue
                current_combo.append(candidate)
                backtrack(i, current_combo, remaining-candidate)
                current_combo.pop()
        
        backtrack(0, [], target)
        return result