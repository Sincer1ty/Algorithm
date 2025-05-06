from collections import deque
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        #n * m 인 던전
        #방에 돌아올때까지 최소 (n-1, m-1)
        #수평, 수직으로 벽을 공유하고 있는 경우 두개의 방이 인접함
        #bfs?
        #이동할 수 있는 최소 시간
        n = len(moveTime)
        m = len(moveTime[0])
        visited = [[float('inf')]*m for i in range(n)]

        def bfs(x,y):
            q = deque()
            q.append((x,y,0)) #x,y, time
            visited[x][y] = 0

            dx = [1,-1,0,0]
            dy = [0,0,1,-1]

            while q:
                x,y,t = q.popleft()
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if 0<=nx<n and 0<=ny<m:
                        #이동시작 시간 
                        arrive = max(t, moveTime[nx][ny])
                        newTime = arrive + 1
                        if newTime < visited[nx][ny]:
                            visited[nx][ny] = newTime
                            q.append((nx,ny, newTime))
                        

        bfs(0,0)
        return visited[n-1][m-1]
        