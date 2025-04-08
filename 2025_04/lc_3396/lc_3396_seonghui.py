class Solution:
    # 고유한지 체크
    def isDistinct(self, nums) -> bool:
        if len(nums) < 3:
            return True
        
        forward = []
        for n in nums:
            # 만약 앞선 리스트에 값이 있으면 안됨
            if n in forward:
                return False
            forward.append(n)
		
        # 슬라이스 해서 확인하는 게 더 빠를지도 고민
        # for i, n in enumerate(nums):
        #     if n in nums[:i]:
        #         return False
        
		# 리스트 안에 같은 값이 몇 개나 들어있는지 확인
        # nums.count(n)
            
        return True
    
    def minimumOperations(self, nums) -> int:
        count = 0
        while not self.isDistinct(nums):
          count += 1
          nums = nums[3:]
        
        return count
