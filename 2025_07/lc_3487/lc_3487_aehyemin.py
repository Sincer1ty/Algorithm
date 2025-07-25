class Solution:
    def maxSum(self, nums: List[int]) -> int:
        #max요소 < 0 이면, 답은 가장 큰 요소
        #0보다 큰 모든 유니크 요소의 합
        num = set(nums)
        ans = 0
        if max(nums) < 0:
            return max(nums)
        else:
            for i in num:
                if i < 0:
                    continue
                else:
                    ans += i
        return ans
            
