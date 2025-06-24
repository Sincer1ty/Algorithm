class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # k-distant 인덱스란,
        # |i-j| <= k 이고, nums[j] == key 인 경우
        # 이 조건을 만족하는 모든 인덱스 i 를 찾아 오름차순으로 정렬된 리스트로 반환
        sets = set()
        n = len(nums)
        for j in range(n):
            if nums[j] == key: #2 , 5
                for i in range(max(0, j-k), min(n, j+k+1)):
                    sets.add(i)
        return sorted(sets)
