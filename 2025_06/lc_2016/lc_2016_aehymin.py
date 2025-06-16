class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        #0 <= i < j < n , nums[i] < nums[j]
        max_val = 0
        n = len(nums)
        for j in range(1, n):
            for i in range(j):
                max_val = max(max_val, nums[j] - nums[i])

        if max_val == 0:
            return -1
        return max_val



        