class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        #n을 2의 거듭제곱들의 합으로 표현할때, 항의 개수가 최소가 되도록 사용하는 2의 거듭제곱들을 오름차순으로 모아 만든 배열을 powers
        #n=15, 1d인비트위치0,1,2,3 (1+2+4+8)
        #queries[l,r] 까지의 곱을 구하라
        mod = 10**9 + 7
        arr = []
        ans = []
        tmp = 1
        while n > 0:
            if n & 1: #마지막 자리가 1인지 체크(1은무조건 끝자리비트만 1)
                arr.append(tmp)
            n >>= 1 #n을 오른쪽으로 1비트
            tmp <<= 1 #tmp를 왼쪽으로 1비트 2*tmp값
        print(arr)

        for i in range(len(queries)):
            l = queries[i][0]
            r = queries[i][1]
            score = 1

            for j in range(l,r+1):
                score =(score * arr[j]) % mod
            ans.append(score)

            
        return ans

        