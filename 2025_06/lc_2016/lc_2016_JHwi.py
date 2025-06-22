class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        big = -1
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] >= nums[j]:
                    continue
                elif nums[j] - nums[i] > big:
                    big = nums[j] - nums[i]
        return big