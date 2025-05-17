class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7

        # 아직 반복 안했을 땐 모두 1글자만 생성
        length = [1] * 26

        # 한번 반복시 다음 알파벳으로 변함
        for _ in range(t):
            nxt = [0] * 26

            # a~y : 한 칸 왼쪽으로 복사
            for c in range(25):       # 0~24
                nxt[c] = length[c + 1]

            #  z 는 a와 b 칸에 글자 수를 더해줌
            nxt[25] = length[0] + length[1]

            # 다음 루프에서는 바뀐 알파벳으로 이어서 반복해야함
            length = nxt

        # s의 글자들을 표에서 꺼내 모두 더한다
        ans = 0
        for ch in s:
            ans += length[ord(ch) - 97] # 97 이 아스키 a 인데 s의 해당 문자의 아스키에 -97을 하면 해당 알파벳의 lengt의 인덱스가 나옴
            ans %= MOD

        return ans
