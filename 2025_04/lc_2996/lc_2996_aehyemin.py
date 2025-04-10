# 포기 합니다
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def at_most(x):
            str_x = str(x)
            ans = 0
            
            for i in range(len(str_x) - len(s)):
                #접미사 자리 빼고 앞 부분 처리
                ans += min(limit + 1, int(str_x[i]))*(limit + 1)** (len(str_x) - len(s)-i-1)
                if int(str_x[i]) > limit:
                    break
            else:
                ans += (int(str_x[-len(s):]) >= int(s))
            return ans

        return at_most(finish) - at_most(start-1)