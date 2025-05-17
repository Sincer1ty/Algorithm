class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        n = len(s)
        temp = s
        for _ in range(t):
            result = ''
            for i in temp:
                if i == 'z':
                    result += 'ab'
                else:
                    result += chr(ord(i) + 1)
            temp = result
        return len(result) % (10**9 + 7)




# 문자를 다음 알파벳 순서로 바꾸는거니 아스키 코드 쓰면 댈듯?
# 은... 타임리미트트