class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result: list[int] = [-1 for i in range(len(arr))]
        currentMax = -float("inf")
        for i in range(len(arr) - 2, -1, -1):
            result[i] = max(currentMax, arr[i + 1])
            currentMax = max(currentMax, arr[i + 1])
        print(result)
        return result