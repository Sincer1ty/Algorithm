class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #중복이 없어야함
        #하나의 하위 배열을 지워서 얻을 수 있는 가장 큰 점수
        #슬라이딩 윈도우
        sets = set()
        l = 0
        score = 0
        ans = 0

        for r, i in enumerate(nums):
            while i in sets:
                sets.remove(nums[l])
                score -= nums[l]
                l += 1
               
            sets.add(i)
            score += i

            ans = max(score, ans)
        return ans

        


