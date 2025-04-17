class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        #nums[i] == nums[j] and (i*j)가 k 로 나누어짐
        # (0 <= i < j < n)
        n = len(nums)
        cnt = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] == nums[j]:
                    if i*j % k == 0:
                        cnt += 1
        return cnt
