# differences[i] = hidden[i+1] - hidden[i]
# if differences = [1, -3, 4]
# hidden[1] = hidden[0] + 1
# hidden[2] = hidden[1] - 3 = hidden[0] + 1 - 3
# hidden[3] = hidden[2] + 4 = hidden[0] + 1 - 3 + 4
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        current = 0
        prefix_sums = [0]
        
        for diff in differences:
            current += diff
            prefix_sums.append(current)
        
        min_val = min(prefix_sums)
        max_val = max(prefix_sums)
        
        # 시작 숫자가 x라면,
        # x + min_val >= lower
        # x + max-val <= upper
        # x >= lower - min_val
        # x <= upper - max_val
        
        min_start = lower - min_val
        max_start = upper - max_val
        
        if max_start < min_start:
            return 0
        return max_start - min_start + 1