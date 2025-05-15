class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        #문자열 배열과, 이진 배열이 주어짐. 길이 같음. 둘은 연관됨
        if len(words) == 1:
            return words
        if len(set(groups)) == 1:
            return [words[0]]

        result = [words[0]]
        for i in range(1, len(words)):
            if groups[i] != groups[i-1]:
                result.append(words[i])
            
        return result

        