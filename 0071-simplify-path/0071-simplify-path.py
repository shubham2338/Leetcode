class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        res=''
        for i in path+'/':
            if i=='/':
                if res=='..':
                    if st: st.pop()
                elif (res!='' and res!='.'):
                    st.append(res)
                res=''
            else:
                res+=i
        return '/'+'/'.join(st)
                
        