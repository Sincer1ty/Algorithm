class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        #basket[j] 는 j번째 바구니의 용량, fruits[i] 는 i번째 과일의 용량
        #왼쪽부터 오른쪽으로 과일 배치
        #크거나 같은 바구니의 용량에 과일 넣기
        #하나의 바구니에는 과일 한종류만
        #놓을수 없는 경우 냅두기
        #배치되지않은 과일의 수 리턴

        ans = 0
        #과일을 기준으로 놓자
        for i in fruits:
            ok = False
            for idx, val in enumerate(baskets):
                if i <= val:
                    baskets.pop(idx)
                    ok = True
                    break
            if not ok:
                ans += 1
       
            
        return ans



        