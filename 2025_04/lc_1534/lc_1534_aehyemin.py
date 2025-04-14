class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for k in range(len(arr)):
            for j in range(k):
                    for i in range(j):
                        if abs(arr[i] - arr[j]) <= a:
                            if abs(arr[j]-arr[k]) <= b:
                                if abs(arr[i] - arr[k]) <= c:
                                    cnt += 1
        return cnt


                    
        