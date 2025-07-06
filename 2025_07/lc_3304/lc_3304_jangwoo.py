class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        
        while len(word) < k:
            new_word = ""
            for ch in word:
                if ch == "z":
                    new_word += "a"
                else:
                    new_word += chr(ord(ch)+1)
            word += new_word
        return word[k-1]