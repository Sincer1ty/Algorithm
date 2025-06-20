class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        #빈도가 낮은 숫자로 변경하기 (N,S) (W,E)
        #토탈 넘버가 k보다 크면, k개를 수정하면 거리가 2k만큼 증가
        #토탈 넘버가 k보다 작거나 같으면, 모든 글자를 수정할 수 있다. 
        #이 경우 맨해튼 거리는 문자열의 길이와 같아짐
        north = south = east = west = 0

        ans = 0
        n = len(s)
        for i in range(n):
            if s[i] == "N":
                north += 1
            elif s[i] == "S":
                south += 1
            elif s[i] == "W":
                west += 1
            elif s[i] == "E":
                east += 1
            one = min(north, south, k)
            two = min(west, east, k-one)
            ans = max(ans, self.count(north, south, one) + self.count(west,east, two))
        return ans

    def count(self, dis1: int, dis2: int, time: int) -> int:
        return (abs(dis1-dis2) + time*2)
        #abs(dis1-dis2) 는 순거리 , time*2 는 바꿀때마다 증가하는 거리

        