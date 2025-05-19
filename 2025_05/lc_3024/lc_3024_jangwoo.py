class Solution:
    def triangleType(self, nums: List[int]) -> str:
        side1,side2,side3 = sorted(nums)
        
        # 이등변 삼각형
        # 변 두개가 길이가 같고, 밑변에 있는 두개의 각이 같다.
        
        # 삼각형
        # 모든 변의 길이가 같으면 정삼각형
        
        # 부등변삼각형
        # 세변의 길이가 모두 다르면 부등변삼각형

        if side1+side2 <= side3:
            return "none"

        if side1 == side2 == side3:
            return "equilateral"

        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "isosceles"

        return "scalene"
        
        