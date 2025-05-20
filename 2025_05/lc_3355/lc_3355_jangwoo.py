# class Solution:
#     def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
#         for i in queries:
#             # 이때 i = [0,2]
#             for j in range(i[0],i[1]+1):
#                 nums[j] -= 1
#                 if nums[j] == -1:
#                     nums[j] = 0
#                 #nums = [0,0,0]
        
#         for k in nums:
#             if k == 0:
#                 pass
#             else:
#                 return False
#         return True
    
# -----------------------------------------------------------------------------------  

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        sibal = [0] * (len(nums)+1)
        
        add_sum = 0
        for i in queries:
            # queries = [[0,2],[1,3]]
            # [-1,0,0,1]
            # 시작점 -1
            # 끝점 1
            # 오 시발! 누적으로 빼준다고? 아!!!!!!
            x,y = i # x = 0, y = 2
            sibal[x] -= 1
            sibal[y+1] += 1
            # [-1,-1,0,1] -> 시발배열 완성
        
        for index_num, value_sum in enumerate(sibal):
            # index_num = 0,1,2,3 
            add_sum += value_sum
            if index_num + 1 == len(sibal):
            #       3          4
                continue
            nums[index_num] += add_sum
            if nums[index_num] <= 0:
                pass
            else:
                return False
        return True
            
            
            
            