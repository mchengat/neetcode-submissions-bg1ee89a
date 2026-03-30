class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result: list[int] = [-1 for i in range(len(arr))]
        currentMax = -1
        for i in range(len(arr) - 1, -1, -1):
            result[i] = currentMax
            currentMax = max(currentMax, arr[i ])
        print(result)
        return result