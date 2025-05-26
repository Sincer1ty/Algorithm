class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(queries)
        m = len(nums)
        arr = [0] * m

        for i in range(n):
            a = queries[i][0]
            b = queries[i][1]
            for j in range(a, b + 1):
                arr[j] += 1
        for k in range(m):
            if nums[k] - arr[k] > 0:
                return False
        return True


