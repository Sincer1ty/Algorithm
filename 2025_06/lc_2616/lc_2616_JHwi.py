class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        if p <= 0:
            return 0
        nums.sort() #정렬해서 왼쪽부터 볼거

        def ssangssangbar(maxdif):
            ssang = 0
            i = 0
            while i < n-1:
                if nums[i+1]-nums[i] <= maxdif:
                    ssang += 1
                    i+=2 # 두개 쌍지었으니 두칸 넘어가야 함
                else:
                    i+=1
                if ssang >= p:
                    return True
            return False
        low = 0
        high = nums[-1] - nums[0]
        while low < high:
            mid = (low+high)//2
            if ssangssangbar(mid):
                high = mid
            else:
                low = mid + 1
        return low
