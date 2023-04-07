class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i,j,grid):
            if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0):
                return 0
            grid[i][j]=0
            return 1+dfs(i+1,j,grid)+dfs(i-1,j,grid)+dfs(i,j-1,grid)+dfs(i,j+1,grid)
        res=0
        res1=0
        for i in grid:
            res+=sum(i)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if((i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1) and grid[i][j]==1):
                    res1+=dfs(i,j,grid)
        return res-res1