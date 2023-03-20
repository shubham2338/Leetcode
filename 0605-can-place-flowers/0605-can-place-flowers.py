class Solution(object):
    def canPlaceFlowers(self, fl, n):
        res=0
        fl=[0]+fl
        fl.append(0)
        for i in range(1,len(fl)-1):
            if fl[i-1]==0 and fl[i]==0 and fl[i+1]==0:
                res+=1
                fl[i]=1
        print(res)
        if res>=n:
            return True
        return False
            
        
        
                
        
        