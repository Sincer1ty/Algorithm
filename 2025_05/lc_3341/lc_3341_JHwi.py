import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        heap = [(0, 0,0)] # 현재 시간, x, y

        visited = [[False] * m for _ in range(n)]

        direction = [(0,1),(1,0),(-1,0),(0,-1)]

        while heap:
            timeNow, x, y = heapq.heappop(heap)
            if visited[x][y] == True:
                continue
            visited[x][y] = True

            # 끝에 도착했다면 시간 리턴
            if x==n-1 and y == m-1:
                return timeNow
            
            for dx, dy in direction:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    next_time = max(timeNow, moveTime[nx][ny]) + 1
                    heapq.heappush(heap, (next_time, nx, ny))
