class Solution:
    def maxSum(self, nums: List[int]) -> int:
        uniq = set(nums)
        arr = []
        for i in uniq:
            if i < 0:
                continue
            arr.append(i)
        if len(arr) <= 1:
            return max(uniq)
        return sum(arr)