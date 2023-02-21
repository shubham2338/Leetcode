class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        while i<j:
            m=(i+j)//2
            if (m%2==1 and nums[m]==nums[m-1]) or (m%2==0 and nums[m+1]==nums[m]):
                i=m+1
            else:
                j=m
        return nums[i]
        
            
        
            