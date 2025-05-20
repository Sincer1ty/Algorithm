class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        #transform 후에 zero array 로 반환할 수 있으면 true, 아니면 false
        #각각의 쿼리[i]에 대해,
        #1. [l,r]범위 내, 하위 집합을 선택한다.
        #2. 선택된 인덱스 값을 1씩 감소시킨다.
        for j in range(len(queries)):
            l = queries[j][0] 
            r = queries[j][1]

            for i in range(l,r+1):
                if nums[i] == 0:
                    continue
                nums[i] -= 1

        a = set(nums)

        if len(a) == 1 and 0 in a:
            return True
        return False


      
                
                

                

