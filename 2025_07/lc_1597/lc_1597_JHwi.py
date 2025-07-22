class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        result = '' # 정답으로 반환할 문자열
        same = 1 # 연속 카운트

        result += s[0]
        cur = s[0]
        for i in range(1,n):
            if cur == s[i]: # 현재 글자가 직전 글자랑 같으면
                if same < 2:
                    result += s[i]
                    same += 1
                    cur = s[i]
                else:
                    cur = s[i]
            else:
                result += s[i]
                same = 1
                cur = s[i]
        return result
            
        