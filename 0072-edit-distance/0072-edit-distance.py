class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        log = {}
        
        def minD(w1, w2, i, j):
            if (i, j) in log:
                return log[(i, j)]
            if i==len(w1) and j==len(w2):
                return 0
            if i == len(w1):
                return len(w2) - j
            if j == len(w2):
                return len(w1) - i
            if w1[i] == w2[j]:
                cnt = minD(w1, w2, i+1, j+1)
            else:
                insert = minD(w1, w2, i, j+1)
                delete = minD(w1, w2, i+1, j)
                replace = minD(w1, w2, i+1, j+1)
                cnt = 1 + min(insert, delete, replace)
            log[(i, j)] = cnt
            return cnt
        return minD(word1, word2, 0, 0)