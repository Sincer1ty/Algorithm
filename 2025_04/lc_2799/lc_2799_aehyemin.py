class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        #어레이의 하위배열이 아래의 조건을 만족하면 satisfied 라고 함
        #서브 어레이의 distinct element 가 전체 어레이의 distinct element 와 같으면
        #서로 다른 원소의 개수
        #complete subarray 반환
        #subarray는 비어있지 않은 연속된 부분
        n = len(nums)
        target = len(set(nums))
        cnt = 0
        for i in range(n):
            sets = set()
            for j in range(i,n):
                sets.add(nums[j])
               
                if len(sets) == target:
                    cnt += 1
        return cnt



        