class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        m = len(nums)
        arr = [0] * (m+1)

        for a, b in queries:
            arr[a] += 1
            arr[b+1] -= 1
        print(arr)

        cur = 0
        for i in range(m):
            cur += arr[i]

            if nums[i] - cur > 0:
                return False
            
        return True
