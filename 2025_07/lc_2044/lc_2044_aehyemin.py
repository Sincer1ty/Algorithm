class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        #OR: 한쪽이라도 1이면 1반환
        #모든 부분집합의 최대OR값을 구함-> 최대값이 몇개인지
        #힌트2: 최대 bitwiseOR 은 전체배열의bitwiseOR
        n = len(nums)
        target = 0 #OR의 최댓값
        ans = 0

        #1. 최대bitwiseOR 구하기
        for i in range(n):
            target |= nums[i]


        #2. 최대bitwiseOR인 부분집합의 개수 구하기
        for bit in range(1, 2**n): #1,2..,7. 공집합 제외
            cur = 0
            #bit = 5, 0번과 2번 원소를 포함
            for j in range(n):
                if bit & (1<<j):
                    cur |= nums[j]
            if cur == target:
                ans += 1
        return ans
​