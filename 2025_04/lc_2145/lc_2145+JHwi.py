class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        pre = 0
        min_sum = 0
        max_sum = 0
    
        for diff in differences:
            pre += diff
            min_sum = min(min_sum, pre)
            max_sum = max(max_sum, pre)
    
        min_x = lower - min_sum
        max_x = upper - max_sum
        
        if min_x > max_x:
            return 0
        else:
            return max_x - min_x + 1