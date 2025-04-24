class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0 #완전한 부분배열의 개수 저장
        cnt = len(set(nums)) #부분배열에 등장하는 원소의 개수가 cnt와 같아야 완전한 부분배열
        n = len(nums) 

        for i in range(n):
            s = set()
            for j in range(i,n):
                s.add(nums[j])
                if len(s) == cnt:
                    ans += 1
        return ans