class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        c_max = -1
        for i in range(n - 1, -1, -1):
            temp = arr[i]
            arr[i] = c_max
            c_max = max(c_max, temp)
        return arr