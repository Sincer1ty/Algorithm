class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0, 0, 0] #0, 1, 2
        #빨강, 하양, 파랑 순으로 정렬. 라이브러리 사용금지
        for i in nums:
            cnt[i] += 1
        print(cnt)
        
        i = 0
        for j in range(3):
            for k in range(cnt[j]):
                nums[i] = j
                i += 1
        



