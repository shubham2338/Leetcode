class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0] or grid[n-1][n-1]:return -1
        q=[]
        q.append((0,0,1))
        grid[0][0]=1
        while q:
            a,b,l=q.pop(0)
            if a==n-1 and b==n-1: return l
            for i in range(a-1,a+2):
                for j in range(b-1,b+2):
                    if i>=0 and i<n and j>=0 and j<n and grid[i][j]!=1:
                        grid[i][j]=1
                        q.append((i,j,l+1))
        return -1
                        