class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        for i in range(n):
            k = nums[i]
            arr.append(nums[k])
        return arr
        