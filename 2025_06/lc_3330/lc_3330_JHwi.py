class Solution:
    def possibleStringCount(self, word: str) -> int:
        # 오류는 한번만 발생
        # 인풋에서 엘리스가 입력하고자 했던 값의 경우의 수를 출력하시오
        unique = set(word)
        n = len(word)
        if len(unique) == 1:
            return n

        # 규칙찾음
        # 2번 중복인애는 결과에 +1
        # 3번 이상 중복인 애들은 중복인 만큼 결과에 +n
        # 등장 빈도 계산하면 가능인가?
        # -> 섞여있으면 안된다

        ans = 1
        for i in range(1, n):
            if word[i] == word[i-1]:
                ans += 1
        return ans


        