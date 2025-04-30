class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        #짝수 개수인 자릿수 반환
        cnt = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                cnt += 1
        return cnt
        