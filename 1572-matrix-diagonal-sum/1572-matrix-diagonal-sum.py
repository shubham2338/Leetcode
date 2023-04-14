class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        for i in range(len(mat)):
            s+=mat[i][i]
        c=0
        for j in range(len(mat)-1,-1,-1):
            s+=mat[c][j]
            c+=1
        if len(mat)%2!=0:
            return s-mat[len(mat)//2][len(mat)//2] 
        return s