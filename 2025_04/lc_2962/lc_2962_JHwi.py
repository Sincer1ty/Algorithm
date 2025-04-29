class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        maxCount = 0
        n = len(nums)
        maxN = max(nums)

        l = 0
        r = 0

        for r in range(n):
            if nums[r] == maxN:
                maxCount += 1
            while maxCount >= k:
                count += n - r
                if nums[l] == maxN:
                    maxCount -= 1
                l += 1
        return count            
