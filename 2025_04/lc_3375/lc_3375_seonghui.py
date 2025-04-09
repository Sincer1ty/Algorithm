class Solution:
    def minOperations(self, nums, k: int) -> int:
        # set로 형변환
        min_val = min(nums)
        if min_val < k:
            return -1
        # 가장 작은 수가 k 와 같으면
        elif min_val == k:
            return len(set(nums))-1
        else:
            return len(set(nums))
