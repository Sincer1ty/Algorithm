class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = set("aeiouAEIOU")
        vowels = False
        consonant = False
        
        #영문자 또는 숫자
        for char in word:
            if char.isdigit():
                continue
            if char.isalpha():
                if char in vowel:
                    vowels = True
                else:
                    consonant = True
            else:
                return False

        if consonant== True and vowels == True:
            return True
        else:
            return False

        
        




        