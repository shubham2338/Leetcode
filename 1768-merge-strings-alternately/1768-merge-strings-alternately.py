class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        res=''
        i=0
        while i<len(w1) and i<len(w2):
            res+=w1[i]
            res+=w2[i]
            i+=1
        if i==len(w1):
            res+=w2[i:]
        else:
            res+=w1[i:]
        return res