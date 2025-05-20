class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        #transform 후에 zero array 로 반환할 수 있으면 true, 아니면 false
        #각각의 쿼리[i]에 대해,
        #1. [l,r]범위 내, 하위 집합을 선택한다.
        #2. 선택된 인덱스 값을 1씩 감소시킨다.
        #[2,1,3] 이면 [[0,2]] 중 원하는 곳만 골라 -1, 3번 수행가능
        n = len(nums)
        diff = [0] * (n+1)

        for l, r in queries:
            diff[l] += 1
            diff[r+1] -= 1

        prefix = 0
        for i in range(n):
            prefix += diff[i]

            if prefix < nums[i]:
                return False
        return True
        

      