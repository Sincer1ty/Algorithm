from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)

        ans = 0

        for i in count:
            if i+1 in count: #해시를 정렬하지 않아도 됨
                ans = max(ans, count[i] + count[i+1])
        return ans