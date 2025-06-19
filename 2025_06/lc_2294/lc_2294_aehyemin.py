class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        #nums를 하나 이상의 정수로 분해할 수 있음
        #각 집합의 최대값과 최소값이 최대 k가 되도록 해라
        #1.일단 정렬
        nums.sort()
        #2.배열을 뺏을때 k값을 초과하는 부분을 분기점으로 잡으면 될듯
        ans = 1 #자기자신
        tmp = nums[0]
        for i in range(1,len(nums)):
            if nums[i] - tmp > k:
                ans += 1
                tmp = nums[i]
        return ans
