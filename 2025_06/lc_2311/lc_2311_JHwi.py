class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # 0 개수를 새자
        zeroNum = s.count('0')
        longN = zeroNum
        val = 0
        bit = 1

        for i in reversed(s): # 오른쪽부터
            if i == '1' and val + bit <= k:
                longN += 1
                val += bit
            bit <<= 1
            if bit > k:
                break
        return longN


