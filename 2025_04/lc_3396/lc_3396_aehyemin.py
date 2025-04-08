from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #앞부터 3개의 요소를 제거했을떄 남은 요소가 3개보다 적으면 모든 요소 지우기
        #빈 배열은 구변되는 요소를 가지고 있는것
        #구별되게 만드는 데 필요한 작업 횟수
        cnt = 0
        while len(nums) > 0:
            if len(set(nums)) == len(nums):
                return cnt
            nums = nums[3:]
            cnt+=1
        return cnt
        
        