class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        keyIndex = []
        result = []
        for i in range(n):
            if nums[i] == key:
                keyIndex.append(i)

        for i in keyIndex:
            start = max(0, i - k)
            end = min(n-1, i + k)
            for j in range(start, end+1):
                result.append(j)
        return list(set(result))

