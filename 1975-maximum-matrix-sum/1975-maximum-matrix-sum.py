class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res=0
        s=987654567898765
        c=0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                r=matrix[i][j]
                s=min(s,abs(r))
                if r<0:
                    c+=1
                res+=abs(r)
        if c%2==0: return res
        else:
            return res-s*2