class Solution(object):
    def zeroFilledSubarray(self, nums):
        ans=0
        i=0
        while i <len(nums):
            c=0
            while i<len(nums) and nums[i]==0:
                c+=1
                ans+=c
                i+=1
            i+=1
        return ans
        
                
                    