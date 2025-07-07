class Solution:
    def kthCharacter(self, k: int) -> str:
        # a에 연산 한번하면 ab 두번하면 abbc
        # 연산해서 나온 문자열의 길이가 k 가 되면 와일문 탈출하게
        # 아스키코드 a = 97 , z = 122

        #반복할때 현재 문자열과 현재 문자열의 다음 문자열을 저장할 임시 변수 필요

        word = ['a']
        while len(word) < k:
            n = len(word)
            nextChars = [] # 연산해서 원본에 추가해야 할 문자들 보관 리스트
            for i in range(n):
                now = word[i]
                if now == 'z':
                    nextCh = 'a'
                else:
                    nextCh =  chr(ord(now) + 1)
                nextChars.append(nextCh)
            word += nextChars
        return word[k-1] # k번째 문자니까 k+1 
