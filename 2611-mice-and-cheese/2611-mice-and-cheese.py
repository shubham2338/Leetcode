class Solution:
    def miceAndCheese(self, r1: List[int], r2: List[int], k: int) -> int:
        d=[]
        for i in range(len(r1)):
            d.append([r1[i]-r2[i],i])
        d.sort(reverse=True)
        res=0
        c=0
        for i in range(k):
            res+=r1[d[i][1]]
            c+=1
        for j in range(c,len(r1)):
            res+=r2[d[j][1]]
        return res
        
        