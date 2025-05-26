class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(queries)
        m = len(nums)

        for i in range(n):
            a = queries[i][0]
            b = queries[i][1]
            for j in range(a, b + 1):
                if nums[j] == 0:
                    continue
                else:
                    nums[j] -= 1
        print(nums)
        arr = []
        for k in range(m):
            arr.append(0)
        if nums == arr:
            return True
        return False

