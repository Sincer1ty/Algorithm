class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        #1~n 인 배열
        #m으로 나눠지지 않는 num1, m으로 나눠지는 num2
        result1 = []
        result2 = []
        for i in range(1,n+1):
            if i % m == 0:
                result2.append(i)
            else:
                result1.append(i)

        return sum(result1) - sum(result2)
        