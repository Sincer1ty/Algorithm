class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        left = 0
        right = 0
        total = 0

        for right in range(n):
            total += nums[right]

            while left <= right and total*(right - left +1) >= k:
                total -= nums[left]
                left += 1


            count += (right - left + 1)
        return count



        # total*(right - left +1)
        