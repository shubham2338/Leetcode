class Solution {
public:
    int numEnclaves(vector<vector<int>>& grid) {
        int res=0;
        int res1=0;
        for(int i=0;i<grid.size();i++){
            for(int j=0;j<grid[0].size();j++)
                    res1+=grid[i][j];
        }
        int close_one = 0;
        for(int i=0;i<grid.size();i++){
            for(int j=0;j<grid[0].size();j++){
                if((i==0 || j==0 || i==grid.size()-1 || j==grid[0].size()-1) && grid[i][j]==1)
                    res+= dfs(i,j,grid);
            }
        }
        return res1 - res;
    }
                   
    int dfs(int i,int j,vector<vector<int>> &grid){
        if( i<0 || j<0 || i>=grid.size() || j>=grid[0].size() || grid[i][j]==0)
            return 0;
        
        grid[i][j] = 0;
        
        return 1+dfs(i-1,j,grid)+dfs(i+1,j,grid)+dfs(i,j-1,grid)+dfs(i,j+1,grid);
    }
};