class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        #score는 합계와 길이의 곱으로 정의된다
        # [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
        #k보다 작은 스코어를 반환한다. 서브어레이
        left = 0
        cnt = 0
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]

            while left <= i and cur*(i - left + 1) >= k:
                cur -= nums[left]
                left += 1

            cnt += i - left + 1

        return cnt
            

            