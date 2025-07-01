class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # 만들수 있는 서브배열 중 최대 최소값 차이가 1이 나면서 길이가 가장 긴 배열의 길이 출력

        # 일단 정렬하자
        nums.sort()
        # 슬라이딩 윈도우로 i를 더해주며 i뒤의 원소가 1차이 내에 있는지 검사
        n = len(nums)
        maxlen = 0

        i = 0
        for j in range(n):
            while nums[j] - nums[i] > 1:
                i += 1
            if nums[j] - nums[i] == 1:
                maxlen = max(maxlen, j-i+1)
        return maxlen

