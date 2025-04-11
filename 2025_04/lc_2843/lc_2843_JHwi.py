class Solution(object):
    def countSymmetricIntegers(self, low, high):
        # low 가 1의 자리 수라면 짝수 자리 수부터 시작해도 됨(홀수는 무조건 비대칭 이니까)
        if len(str(low)) % 2 != 0:
            start = 10 ** len(str(low))
        else:
            start = low

        count = 0
        # 나누기로 해결할수 있을것 같은데 홀수 자릿수 일 때 넘기는것도
        for i in range(start,high+1):
            numlen = len(str(i))
            if numlen % 2 != 0:
                continue
            elif numlen == 2:
                n1 = i%10
                n2 = i/10
                if n1 == n2:
                    count += 1
            elif numlen == 4:
                n1 = i%10
                n2 = (i%100)/10
                n3 = (i%1000)/100
                n4 = i/1000
                if n1+n2 == n3+ n4:
                    count += 1
        return count