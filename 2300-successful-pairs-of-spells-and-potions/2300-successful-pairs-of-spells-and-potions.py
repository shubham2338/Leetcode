class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def bs(t,v,arr):
            i=0
            j=len(arr)
            while i<j:
                m=(i+j)//2
                if arr[m]*t>=v:
                    j=m
                else:
                    i=m+1
            return i
                    
        potions.sort()
        ans=[0 for i in range(len(spells))]
        for i in range(len(spells)):
            h=bs(spells[i],success,potions) 
            ans[i]=(len(potions)-h)
        return ans
        