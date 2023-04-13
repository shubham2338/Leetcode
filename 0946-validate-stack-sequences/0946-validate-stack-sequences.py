class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st=[]
        j=0
        for i in pushed:
            st.append(i)
            while st and st[-1]==popped[j]:
                st.pop()
                j+=1
        if st:return False
        return True
        
                
        