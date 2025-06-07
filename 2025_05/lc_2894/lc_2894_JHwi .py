class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = []
        num2 = []
        for i in range(n+1):
            if i % m == 0:
                num2.append(i)
            else:
                num1.append(i)
        return sum(num1) - sum(num2)
        