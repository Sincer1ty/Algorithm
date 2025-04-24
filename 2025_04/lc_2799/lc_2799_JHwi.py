class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        Un= len(set(nums))
        count = 0

        for i in range(n):
            check = set()
            for j in range(i, n):
                check.add(nums[j])
                if len(check)==Un:
                    count += 1
        return count