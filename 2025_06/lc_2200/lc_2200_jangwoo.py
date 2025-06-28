from typing import List  # 반드시 필요!

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        start = 0
        ans = []
        
        for i in range(n):
            if nums[i] == key:
                left = max(0, i - k)
                right = min(n - 1, i + k)  # ← 여기 오타 있었음. 'max' → 'min'으로 고쳐야 해요
                
                while start <= right:
                    if start >= left:
                        ans.append(start)
                    start += 1
        
        return ans
    
# 아래는 테스트용 코드입니다
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 2, 2, 2]
    key = 2
    k = 2
    result = sol.findKDistantIndices(nums, key, k)
    print("결과:", result)