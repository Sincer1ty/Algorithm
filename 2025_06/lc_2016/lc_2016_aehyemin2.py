class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        #0 <= i < j < n , nums[i] < nums[j]
        min_val = nums[0]
        max_val = -1
        n = len(nums)

        for j in range(n):
            if min_val < nums[j]:
                max_val = max(max_val, nums[j]-min_val)
            else:
                min_val = nums[j]
        return max_val
            

       

        