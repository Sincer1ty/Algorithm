class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #순열로 배열 만들기
        #순열 nums 가 주어지면, ans[i] = nums[nums[i]] 인 ans 만들기
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans