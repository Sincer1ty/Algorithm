class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        n0 = set()
        m0 = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    n0.add(i)
                    m0.add(j)
        for i in n0:
            for j in range(m):
                matrix[i][j] = 0
        for i in m0:
            for j in range(n):
                matrix[j][i] = 0





    # 0 이 있는 행 저장
    # 0 이 있는 열 저장
    #저장된 행&열 원소를 모두 0으로
        