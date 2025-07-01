class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        #k이하의 이진수를 표현하는 가장 긴 서브시퀀스
        #0은 다쓰기
        #뒤부터 고려
        ans = 0
        val = 0
        bits = k.bit_length() # 2진수로 나타내는데 몇 비트가 필요한지 5-> 101 3비트필

        for i, char in enumerate(s[::-1]):
            if char == "1":
                if i < bits and val + (1 <<i) <= k:
                #비트수확인하고 값이 k 이하인지 확인
                    val += 1 << i
                    ans += 1
            else:
                ans += 1
        return ans

