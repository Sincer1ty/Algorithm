class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        left = 0
        large = n+1
        #점을 기준으로 계산?
        #왼쪽으로 넘어가는 힘
        #오른쪽으로 넘어가는 힘
        right_f = [large] * n
        f = large

        #오른쪽으로 넘어가는 힘 왼->오
        for i in range(n):
            if dominoes[i] == "R":
                f = 0
            elif dominoes[i] == "L":
                f = large
            else: # . 을 만남. 계산하기
                if f < large:
                    f += 1
            right_f[i] = f

        #왼쪽으로 넘어가는 힘 오->왼
        left_f = [large] * n
        f = large
        for i in range(n-1, -1, -1):
            if dominoes[i] == "L":
                f = 0
            elif dominoes[i] == "R":
                f = large
            else:
                if f < large:
                    f += 1
            left_f[i] = f

        ans = []
        for i in range(n):
            if left_f[i] < right_f[i]:
                ans.append("L")
            elif left_f[i] > right_f[i]:
                ans.append("R")
            else:
                ans.append(".")
        return "".join(ans)
            





        