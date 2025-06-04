class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        #numFriends 를 위한 게임을 준비했다. 멀티플 라운드 게임
        #각각 라운드는, word가 numfriends(공백없이)로 찢어진다, 전 라운드와 같은것은 안됨
        #찢어진 단어를 박스에 넣기
        #min(a.len, b.len) 이 같으면 사전순으로 앞에 오는게 더 작은 수, ㄱ길익가 다르면 짧은쪽이 작은수
        #모든 라운드가 끝난 후 사전순으로 가장 큰 lexicographically string
        #Find lexicographically largest substring of size n - numFriends + 1 or less starting at every index.
        #가장큰 lexi.. 서브스트링의 크기는 n - numFriends + 1 or less starting at every index
        if numFriends == 1:
            return word
        ans = []
        n = len(word)
        lex = n - numFriends + 1 
        # 3
        for i in range(n+1):
            ans.append(word[i:i+lex]) ## word[0::2] , word[1::3]

        max_len = len(max(ans))

        real = []
        for j in ans:
            if len(j) == max_len:
                real.append(j)

        output = real[0]
        for i in range(1,len(real)):
            if output < real[i]:
                output = real[i]
        return output
