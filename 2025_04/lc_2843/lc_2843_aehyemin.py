class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        #대칭: x의 first n digit 합이 x의 last n digit 합과 같으면 대칭이다.
        #x는 2*n 디짓으로 이루어져 있음
        #[low,high] 사이의 대칭 넘버 개수를 리턴하라
        #앞의 반이랑 뒤의 반 합이 같으면 대칭
        cnt = 0
        
        for i in range(low, high+1):
            str_i = str(i)

            if len(str_i) % 2 == 0:
                l = len(str_i)//2
                a = str_i[:l]
                b = str_i[l:]
              
                sum_a = sum(map(int, a))
                sum_b = sum(map(int, b))

                if sum_a == sum_b :
                    cnt += 1

        return cnt




        