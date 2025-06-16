class Solution:
    def maxDifference(self, s: str) -> int:
        uniq = list(set(s))
        check = {}
        for i, ch in enumerate(uniq):
            check[ch] = i

    
        arr = [0] * len(uniq)
        for ch in s:
            arr[check[ch]] += 1

        # 홀수 최대, 짝수 최소 찾기
        maxOdd  = 0
        minEven = len(s) + 1       

        for cnt in arr:
            if cnt % 2: # 홀수일때
                if cnt > maxOdd:
                    maxOdd = cnt
            else: # 짝수일때
                if cnt and cnt < minEven:
                    minEven = cnt
        return maxOdd - minEven
