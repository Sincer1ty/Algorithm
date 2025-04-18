class Solution:
    def countAndSay(self, n: int) -> str:
        #숫자가 쓰인 횟수 + 쓰인 문자 로 문자열을 바꾸기
        #n 번째 요소를 반환하라. 직접 문자열을 구해야함?
        #CAS 는 이전항을 읽는다. CAS(1) = "1"

        if n == 1:
            return "1"
        one = "1"

        for i in range(2, n+1):
            new = ""
            cnt = 1
            #숫자 쓰인횟수 + 쓰인 숫자
            for j in range(1, len(one)):
                if one[j-1] == one[j]:
                    cnt += 1
                else:
                    new += str(cnt) + one[j-1]
                    cnt = 1
            
            new += str(cnt) + one[-1]
            one = new
        return one