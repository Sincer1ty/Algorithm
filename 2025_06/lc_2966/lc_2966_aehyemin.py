class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        #크기가n인 배열 nums, n은 3의 배수이고, 3은 양의 정수k
        #조건을 만족하는 크기가 n/3인 배열로 나누기
        #한 배열의 모든 두 요소의 차이가 k만큼이거나 더 적다
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(0,n,3):
            if nums[i+2] - nums[i] > k:
                return []
            result.append(nums[i:i+3])
        return result
        
        
        



        