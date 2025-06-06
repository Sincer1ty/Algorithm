from collections import Counter
class Solution:
    def robotWithString(self, s: str) -> str:
        #s문자열과 비어있는 문자열t. s와t가 모두 빌때까지 적용한다
        #s의 첫번째 문자를 지워 로봇에게 전달. t에게 문자를 추가
        #t의 마지막 문자를 지워. 로봇은 이 문자를 종이에 쓸거??
        #종이에 쓸수있는 사전적으로 가장 작은 문자열 반환
        t = [] #두번째
        p = [] #출력
        count = Counter(s)
        minChar ="a"
        for i in s:
            t.append(i)
            count[i] -= 1
            print(t)

        #a -> b -> c -> d 
            while minChar != "z" and count[minChar] == 0:
                minChar = chr(ord(minChar) + 1)
            
            while t and t[-1] <= minChar:
                p.append(t.pop())

        # while t:
        #     p.append(stack.pop())
        return "".join(p)



            
        


     