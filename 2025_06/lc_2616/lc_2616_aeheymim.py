class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        #힌트1: 배열을 먼저 정렬한다. -> 선택범위 낭비 줄이기
        nums.sort()
        n = len(nums)
        #힌트2: 이분탐색: p개의 쌍을 만들 수 있는 가장 작은 최대 차이값
        #최대 차이가 x 이하인 쌍을 최소 p 개 만들 수 있는 최소 x를 리턴

        #유효한 쌍의 개수 세는 함수
        def countPairs(x):
            idx = 0
            cnt = 0
            while idx < n-1:
                if nums[idx+1] - nums[idx] <= x:
                    cnt += 1
                    idx += 1
                idx += 1 #두 수 사용됨
            return cnt
        
        #이분탐색
        #mid 는 허용할 차이값 x 
        left = 0 
        right = nums[-1] - nums[0]
        while left < right:
            mid = (left+right) // 2

            if countPairs(mid) >= p:
                right = mid #오른쪽 줄이기
            else:
                left = mid + 1
        return left






        