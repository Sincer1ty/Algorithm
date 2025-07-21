class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = odd = 0 # 짝 홀 개수
        len_even = len_odd = 0 # 교차 끝이 짝/홀 일 때
        for i in nums:
            if i % 2 == 1: #홀수라면
                odd += 1

                len_odd = max(len_odd, len_even + 1)
            else:
                even += 1
                len_even = max(len_even, len_odd + 1)

        return max(even, odd, len_odd, len_even)
