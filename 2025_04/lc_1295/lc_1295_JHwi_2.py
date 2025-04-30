class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            numLen = 0
            while i:
                numLen += 1
                i //= 10
            if numLen%2 == 0:
                count += 1
        return count
            