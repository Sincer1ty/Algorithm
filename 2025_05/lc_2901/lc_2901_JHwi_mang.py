class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        arr = []
        if n == 1:
            return words

        for i in range(1, n):
            if groups[i] != groups[i-1] and words[i] != words[i-1] and len(words[i]) == len(words[i-1]) :
                m = len(words[i])
                cnt = 0
                for j in range(m):
                    if words[i][j] == words[i-1][j]:
                        cnt += 1
                if cnt == m-1:
                    arr.append(words[i-1])
                    arr.append(words[i])
        arr = list(set(arr))
        arr.sort()
        if len(arr) == 0:
            arr.append(words[n-1])
        return arr
    
    # 실패패

