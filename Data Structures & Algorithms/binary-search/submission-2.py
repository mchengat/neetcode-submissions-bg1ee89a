class Solution:
    def binary_search(self, l: int, r: int, nums: list[int], target: int) -> int:
        if l > r:
            return -1
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        if target < nums[m]:
            return self.binary_search(l, m - 1, nums, target)
        return self.binary_search(m + 1, r, nums, target)

    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)