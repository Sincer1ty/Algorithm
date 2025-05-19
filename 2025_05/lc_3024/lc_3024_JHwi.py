class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # c = nums.pop(nums.index(max(nums)))
        # b = nums.pop(nums.index(max(nums)))
        # a = nums.pop(nums.index(max(nums)))
        a, b, c = sorted(nums)

        # 삼각형이 아니면
        if a+b <= c:
            return "none"
        # 정삼각형인 경우
        if a == b == c:
            return "equilateral"
        # 이등변 삼각형
        elif a == b or a == c or b == c:
            return "isosceles"
        #걍 삼각형
        return "scalene"
    