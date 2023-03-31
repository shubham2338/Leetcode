class Solution {
public:
    int n, m;
    long long int dp[51][51][51];
    long long mod= 1e9+7;
    long long int  count(int r, int c, int cuts, vector<vector<int>>&apples){
        if(dp[r][c][cuts]!=-1)return dp[r][c][cuts];
        if(cuts==0){
            dp[r][c][cuts]=(apples[r][c]>0)?1:0;
            return dp[r][c][cuts];
        }
        long long int row=0;
        long long int col=0;
        for(int i=r+1;i<n;i++){
            if (apples[r][c]-apples[i][c] >0 && apples[i][c]>=cuts)
            row=(row+count(i,c,cuts-1,apples))%mod;
        }
        for(int j=c+1;j<m;j++){
            if (apples[r][c]-apples[r][j]>0 && apples[r][c]>=cuts)
                col=(col+count(r,j,cuts-1,apples))%mod;
        }
        dp[r][c][cuts]=row+col;
        return dp[r][c][cuts];
    }
    int ways(vector<string>& pizza, int k) {
        memset(dp,-1,sizeof(dp));
        n=pizza.size();
        m=pizza[0].size();
        vector<vector<int>>apples(n+1,vector<int>(m+1,0));
        for(int i=n-1;i>=0;i--){
            for(int j=m-1;j>=0;j--){
                apples[i][j]=apples[i+1][j]+apples[i][j+1]-apples[i+1][j+1]+(pizza[i][j]=='A');
            }
        }
        long long int ans=count(0,0,k-1,apples);
        return ans;
        
    }
};