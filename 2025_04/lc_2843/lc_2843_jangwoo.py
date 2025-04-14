class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for n in range(low, high + 1):
            s = str(n)
            if len(s) % 2 != 0:
                continue
            mid = len(s) // 2

            left_sum = 0
            for i in range(mid):
                left_sum += int(s[i])

            right_sum = 0
            for i in range(mid, len(s)):
                right_sum += int(s[i])
            
            if left_sum == right_sum:
                cnt += 1
        return cnt
            