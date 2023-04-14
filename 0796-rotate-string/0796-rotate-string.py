class Solution:
    def rotateString(self, s: str, g: str) -> bool:
        c=0
        s=list(s)
        g=list(g)
        while c<=len(s) and s!=g:
            s=list(s)
            c+=1
            s.append(s.pop(0))
        if s==g:
            return True
        return False
        