class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j):
            if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0:
                return False
            if grid[i][j]==1:
                return True
            grid[i][j]=1
            a=dfs(grid,i+1,j)
            b=dfs(grid,i,j+1)
            c=dfs(grid,i-1,j)
            d=dfs(grid,i,j-1)
            return a and b and c and d
        res=0
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    if dfs(grid,i,j):
                        res+=1
        return res
    
        