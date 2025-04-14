class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        length = len(arr)
        count = 0

        for i in range(length-2):
            for j in range(i+1, length-1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, length):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count+=1
                            
        return count