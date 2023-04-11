class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        for i in s:
            if i=='*' and len(st)>0:
                st.pop(-1)
            else:
                st.append(i)
        h=''.join(st)
        return h
                
        