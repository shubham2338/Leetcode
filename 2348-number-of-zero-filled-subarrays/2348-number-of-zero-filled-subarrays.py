import math
class Solution(object):
    def zeroFilledSubarray(self, nums):
        ans=0
        i=0
        j=0
        while i<len(nums):
            if nums[i]!=0:
                j=i+1
            ans+=i-j+1
            i+=1
        return ans
        
                
                    