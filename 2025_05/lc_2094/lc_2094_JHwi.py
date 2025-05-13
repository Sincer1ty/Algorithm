class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
    
        arr = []    
        for i in range(n):
            if digits[i] == 0:  # 첫자리 0 이면 ㅌㅌ
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    arr.append(num)
        return sorted(list(set(arr)))
