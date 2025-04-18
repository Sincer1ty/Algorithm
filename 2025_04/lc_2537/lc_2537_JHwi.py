class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            fr = {}
            pair = 0
            for j in range(i, n):
                num = nums[j]
                if num in fr:
                    pair += fr[num]
                    fr[num] += 1
                else:
                    fr[num] = 1
                if pair >= k:
                    count += 1
        return count


        