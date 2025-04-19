class Solution:
    def countAndSay(self, n: int) -> str:
        def check_sereal(arr):
            result = ""
            count = 1
            pre = arr[0]
            
            for i in range(1, len(arr)):
                if arr[i] == pre:
                    count += 1
                else:
                    result += str(count) + pre
                    pre = arr[i]
                    count = 1
            result += str(count) + pre
            return result

        arr = '1'
        for _ in range(n - 1):
            arr = check_sereal(arr)
        return arr