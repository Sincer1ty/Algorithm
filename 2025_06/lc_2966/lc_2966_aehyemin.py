class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        #크기가n인 배열 nums, n은 3의 배수이고, 3은 양의 정수k
        #조건을 만족하는 크기가 n/3인 배열로 나누기
        #한 배열의 모든 두 요소의 차이가 k만큼이거나 더 적다
        nums.sort()
        n = len(nums)
        num = [nums[i-3:i] for i in range(3, n+1,3)]

        for j in range(len(num)):
            if max(num[j]) - min(num[j]) > k:
                return []
        return num



        