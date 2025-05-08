class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        timeNow = 0





# 현지 시간을 카운트할 timeNow 변수 필요
# 이동에는 1초 소요
# 시간이 흘렀을 때 열리는 문중 가장 값이 작은 인덱스로 이동하는 조건문을 만들자
# 해당[i][j], 오른쪽[i][j+1], 아래[i+1][j]