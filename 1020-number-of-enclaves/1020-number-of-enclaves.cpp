class Solution {
public:
    int numEnclaves(vector<vector<int>>& A) {
        int all_one=0;
        for(int i=0;i<A.size();i++){
            for(int j=0;j<A[0].size();j++)
                    all_one+=A[i][j];
        }
        int close_one = 0;
        for(int i=0;i<A.size();i++){
            for(int j=0;j<A[0].size();j++){
                if((i==0 || j==0 || i==A.size()-1 || j==A[0].size()-1) && A[i][j]==1)
                    close_one+= dfs(i,j,A);
            }
        }
        return all_one - close_one;
    }
                   
    int dfs(int i,int j,vector<vector<int>> &grid){
        if( i<0 || j<0 || i>=grid.size() || j>=grid[0].size() || grid[i][j]==0)
            return 0;
        grid[i][j] = 0;
        return 1+dfs(i-1,j,grid)+dfs(i+1,j,grid)+dfs(i,j-1,grid)+dfs(i,j+1,grid);
    }
};