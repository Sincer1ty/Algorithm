class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        def check_good(arr, x, y, z):
            if abs(arr[x] - arr[y]) <= z:
                return True
            else:
                return False
        # ----------------------------------------- 
        count = 0
        arr_len = len(arr)

        for i in range(arr_len):
            # print(i)
            for j in range(i + 1, arr_len):
                # print('-', j)
                if check_good(arr, i, j, a) == True and i < j:
                    for k in range(j + 1, arr_len):
                        # print(arr[i], arr[j], arr[k])
                        if check_good(arr, j, k, b) == True and check_good(arr, i, k, c) == True and j < k:
                            count += 1
        return count
        