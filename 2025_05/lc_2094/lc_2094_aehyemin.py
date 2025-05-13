from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        #임의의 순서로 세 숫자를 연결해
        #정수는 leading zero (0으로시작 하는 정수) 가 아
        #정수는 짝수
        sets = set()

        for i in permutations(digits, 3):
            if i[0] == 0:
                continue

            if i[2] % 2 != 0:
                continue
            
            num = i[0]*100 + i[1]*10 + i[2]
            sets.add(num)
        
        return sorted(sets)
        
        