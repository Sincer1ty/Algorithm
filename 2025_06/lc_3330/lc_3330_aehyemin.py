class Solution:
    def possibleStringCount(self, word: str) -> int:
        #마지막에 나온 결과물로 원래 쓰려던 문자 유추
        ans = 1 #최대 한번 이므로, word 그대로 일수도 있음
        #a 실수0, b는 실수1, c는 실수 1번2번3번 
        
        for i in range(1, len(word)):
            if word[i-1] == word[i]:
                ans += 1

        return ans

        