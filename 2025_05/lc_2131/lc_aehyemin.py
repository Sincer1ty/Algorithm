class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        mid = False
        print(count)

        for word in count:
            rev = word[::-1]

            #단어가 펠린드롬
            if word == rev: #뒤집은거랑 같으면, aa
                pairs = count[word] // 2
                length += pairs * 4 # 2 + 2
                
                if count[word] % 2 == 1:
                    mid = True
                    #펠린드롬 정가운데 배치

            #펠린드롬이 아니면, ab
            elif rev in count:
                pairs = min(count[rev], count[word])
                length += pairs * 4

                count[word] = 0
                count[rev] = 0

        if mid == True:
            length += 2

        return length


        