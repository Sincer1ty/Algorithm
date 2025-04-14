class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        cnt = 0
        long = len(arr)
        
        for i in range(long-2):
            for j in range(i+1,long-1):
                if (abs(arr[i]-arr[j]) <= a):
                    for k in range(j+1,long):
                        if (abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c):
                            cnt +=1
        return cnt