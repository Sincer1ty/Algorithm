class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
    #h보다 크면 유효
    #현재 배열에 valid 한 정수 h를 고른다
    #num[i]>h 인 원소를 모두 h로 바꾼다
    #두번째로 큰 수부터 바꾸기
        if min(nums) < k :
            return -1
        sets = set()

        for i in nums:
            if i>k and i not in sets:
                sets.add(i)
        return len(sets)