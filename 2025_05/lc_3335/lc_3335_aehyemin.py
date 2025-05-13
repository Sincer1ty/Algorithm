class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        #Z 면 ab로 바꾼다
        #a->b, b-c
        #t번 변환을 마친 후, 문자열 길이 모듈러 연산
        #길이저장
        alpha = [0] * 26
        mod = 10**9 + 7

        for i in s:
            alpha[ord(i)- 97] += 1

        for j in range(t):
            new_al = [0] * 26

            for k in range(25):
                new_al[k+1] = (new_al[k+1] + alpha[k]) % mod

            new_al[0] = new_al[0] + alpha[25] % mod
            new_al[1] = new_al[1] + alpha[25] % mod

            alpha = new_al


        return sum(alpha) % mod


        