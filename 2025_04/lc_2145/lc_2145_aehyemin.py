class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        #differences[i] = hidden[i + 1] - hidden[i]
        #hidden sequence 범위 lower upper
        #dif[0] = hidden[1] - hidden[0] = 1
        #dif[1] = hidden[2] - hidden[1] = -3
        #dif[2] = hidden[3] - hidden[2] = 4
        #hidden[1] = x + differences[0]
        #hidden[2] = x + differences[0] + differences[1]
        #hidden[3] = x + differences[0] + differences[1] +  differences[2]
        #lower<= x+prefix[i] <= upper
        cur = 0
        min_i = 0
        max_i = 0

        for i in differences:
            cur += i
            min_i = min(min_i, cur)
            max_i = max(max_i, cur)

        low = lower - min_i
        high = upper - max_i

        return max(high - low + 1, 0)
