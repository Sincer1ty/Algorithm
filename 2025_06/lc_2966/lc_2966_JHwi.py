class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # 정수형 배열 nums, 정수 k(양수) 주어짐
        # n = len(nums)
        # n % 3 == 0 (n 은 3의 배수)
        # nums 를 3개의 원소를 가진 서브 트리로 전부 나눠서 2차원 배열을 만든후
        # 모든 서브 어레이가 max(a, b, c) - min(a, b, c) <= k 를 만족하면 출력 아니면 빈 어레이 출력

        n = len(nums)
        nums.sort()
        
        result = []

        for i in range(0,n,3):
            temp = nums[i:i+3]
            if max(temp) - min(temp) > k:
                return []
            result.append(temp)
        return result
