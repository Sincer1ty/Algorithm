import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # timeNow = 0
        n = len(moveTime)
        m = len(moveTime[0])

        heap = [(),(),()] # 현재 시간, x, y

        visited = [[False] * m for _ in range(n)]

        direction = [(0,1),(1,0),(-1,0),(0,-1)]

        while heap:
            timeNow, x, y = heap
            if visited[x][y] == True
                continue
            visited[x][y] = True

            




# 현지 시간을 카운트할 timeNow 변수 필요
# 이동에는 1초 소요

# 시간이 흘렀을 때 열리는 문중 가장 값이 작은 인덱스로 이동하는 조건문을 만들자
# 해당[i][j], 오른쪽[i][j+1], 아래[i+1][j] ... 해서
# 비교하면서 하면 되려나?