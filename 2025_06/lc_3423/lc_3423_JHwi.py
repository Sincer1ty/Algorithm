class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        # abs
        # 인접 값의 차 절댓값중 가장 큰값을 골라
        # 순회를 돌면서 둘중 큰 값에서 작은값을 빼자
        # 뺀 값을 저장한 맥스값과 비교해서 더 크면 현재 값을 맥스로
        maxNum = 0
        for i in range(n):
            cur = 0
            if i == n-1:
                a = nums[i]
                b = nums[0]
            else:
                a = nums[i]
                b = nums[i+1]
            if a>b:
                cur = abs(a-b)
            else:
                cur = abs(b-a)
            if cur > maxNum:
                maxNum = cur
        return maxNum


        