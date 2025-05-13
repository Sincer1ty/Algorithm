import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        if n == 1 and m == 1:
            return 0

        visited = [[float('inf')] *m for i in range(n)]
        visited[0][0] = 0

        #지금까지 걸린시간, x, y, step
        q = [(0,0,0,0)]

        while q:
            t, x, y, s = heapq.heappop(q)
            if (x,y) == (n-1, m-1):
                return t

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                u, v = x + dx, y + dy
                if 0<=u<n and 0<=v<m:
                    movement = 1 if s % 2 == 0 else 2
                    arrive = max(t, moveTime[u][v]) + movement
                    if arrive < visited[u][v]:
                        visited[u][v] = arrive
                        heapq.heappush(q, (arrive,u,v, s+1))
                    

        return -1
