class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        #원형 어레이가 주어짐, 인접한 요소 두개 사이 가장 큰 큰 절댓값
        new_num = nums*2

        result = []
        for i in range(1,len(new_num)):
            result.append(abs(new_num[i-1]-new_num[i]))

        return max(result)
