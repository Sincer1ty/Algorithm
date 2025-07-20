class Solution:
    def makeFancyString(self, s: str) -> str:
        #fancy: 연속된 세 문자가 같지 않은 문자, eee 안됨
        new = []
        for i in range(len(s)):
            if len(new) >= 2 and new[-1] == s[i] and new[-2] == s[i]:
                continue
            new.append(s[i])
        return "".join(new)
            
