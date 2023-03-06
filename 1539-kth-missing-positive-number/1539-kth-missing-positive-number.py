class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        k+=1
        ans=[0]*(1000000)
        for i in arr:
            ans[i]=1
        res=0
        for i in range(len(ans)):
            if ans[i]==0:
                k-=1
                res=i
            if k<=0:
                break
      
        return res
                