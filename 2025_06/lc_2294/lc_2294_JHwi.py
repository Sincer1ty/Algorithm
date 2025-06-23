class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # 정수배열 nums, 정수k 주어짐
        # 배열을 서브시퀀스로 나눌건디
        # 연속되는 수열로 나눌건데
        # 123, 567 이렇게 끊어질때 까지 하나로 엮어서 나눌거
        # 서브배열 최대 - 최소 가 k 이하여야함 
        # 그렇게 나눈다면 몇개의 서브 어레이가 필요한지를 반환
  
        n = len(nums)
        nums.sort()
        count = 1
        head = nums[0]

        for i in range(n):
            if nums[i] - head > k:
                count += 1
                head = nums[i]
        return count
