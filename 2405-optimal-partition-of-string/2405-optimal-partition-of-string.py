class Solution:
    def partitionString(self, s: str) -> int:
        res=1
        j=0
        r=''
        while j<len(s):
            if s[j] in r:
                r=''
                res+=1
                j-=1
            else:
                r+=s[j]
            j+=1
        return res
        
                
            
                