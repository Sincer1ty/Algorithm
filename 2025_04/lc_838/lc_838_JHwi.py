class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        cur = list(dominoes)
        while True:
            new = cur.copy()
            changed = False

            for i in range(n):
                # 이미쓰러진 벽돌
                if cur[i] != '.':
                    continue
                # L방향 힘이 있으려면 i+1 벽돌이 있고 그 벽돌이 L 이여햐 함
                LeftForce = (i < n-1   and cur[i+1] == 'L')
                # R방향 힘이 있으려면 i-1 벽돌이 있고 그 벽돌이 R 이여햐 함
                RighForce = (i > 0  and cur[i-1] == 'R')

                if LeftForce and not RighForce:
                    new[i] = 'L'
                    changed = True
                elif RighForce and not LeftForce :
                    new[i] = 'R'
                    changed = True
            if changed == False:
                break
            cur = new
        return ''.join(cur)