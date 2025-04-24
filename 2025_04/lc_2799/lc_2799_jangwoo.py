class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0 #완전한 부분배열의 개수 저장
        cnt = len(set(nums)) #부분배열에 등장하는 원소의 개수가 cnt와 같아야 완전한 부분배열
        n = len(nums) 

        for i in range(n): # 부분배열의 길이는 주어진 배열의 길이 이상이 될 수 없기에 주어진 배열의 길이만큼만 탐색 
            s = set()
            for j in range(i,n):
                s.add(nums[j])
                if len(s) == cnt:
                    ans += 1
        return ans