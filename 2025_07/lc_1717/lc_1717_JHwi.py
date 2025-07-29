class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # x, y 중 점수가 더 큰애를 먼저 빼주자

        def remover(s, fst, sec, score):
            stack = []
            point = 0
            for i in s:
                if stack and stack[-1] == fst and i == sec:
                    stack.pop()
                    point += score
                else:
                    stack.append(i)
            return ''.join(stack), point

        if x > y:
            s, point1 = remover(s, 'a', 'b', x)
            _, point2 = remover(s, 'b', 'a', y)
        else:
            s, point1 = remover(s, 'b', 'a', y)
            _, point2 = remover(s, 'a', 'b', x)

        return point1 + point2

        