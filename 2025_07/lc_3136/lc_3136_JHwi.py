class Solution:
    def isValid(self, word: str) -> bool:
        # 3자이상
        # 숫자 영문자 대소만
        # 모음 하나이상 포함 aeiou
        # 자음 하나이상 포함 else
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

        vowel_found = False
        consonant_found = False

        consonant = []
        n = len(word)

        if n < 3: # 3 글자 필터
            return False

        for i in word:
            if i in '1234567890': #  숫자면 검사 넘어감
                continue

            ch = ord(i)
            if not(65 <= ch <= 90 or 97 <= ch <= 122): # 숫자 영문자 필터
                return False
            if i in vowel: # 모음 하나 이상 있는가
                vowel_found = True
            else: # 자음 하나 이상 있는가
                consonant_found = True

        if vowel_found and consonant_found:
            return True
        return False
            