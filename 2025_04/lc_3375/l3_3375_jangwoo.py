from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for n in nums:
            if n < k:
                return -1
        
        single_nums = set(nums)
        cnt = 0

        for x in single_nums:
            if x > k:
                cnt += 1
        
        return cnt