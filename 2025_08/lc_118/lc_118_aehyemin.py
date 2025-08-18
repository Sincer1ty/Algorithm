class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <=0 :
            return [[]]
        a = [[1]]

        for i in range(1, numRows):
            prev = a[i-1]
            row = [1]
            
            for j in range(1,i):
                row.append(prev[j] + prev[j-1])
            row.append(1)
            a.append(row)
   
        return a
                
