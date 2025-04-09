class Solution(object):
    def minOperations(self, nums, k):
        m = min(nums)
        unique = set(nums)
        if m < k:
            return -1
        elif m > k:
            return len(unique)
        else:
            return len(unique)-1