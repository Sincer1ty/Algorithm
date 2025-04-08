class Solution(object):
    def minimumOperations(self, nums):
        def is_unique(arr):
            return len(arr) == len(set(arr))

        count = 0

        while len(nums) > 0:
            if is_unique(nums):
                return count
            if len(nums) < 3:
                nums = []
            else:
                nums = nums[3:]
            count += 1

        return count
