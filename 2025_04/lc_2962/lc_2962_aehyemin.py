from collections import defaultdict
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        #최대 요소가 적어도 k번 나타나는 하위배열의 개수 반환
        max_num = max(nums)
        n = len(nums)
        left = 0
        cnt = 0
        hash = defaultdict(int)
        
        for right in range(len(nums)):
            hash[nums[right]] += 1 

            while hash[max_num] >= k:
                cnt += n - right
                hash[nums[left]] -= 1
                left += 1
        return cnt