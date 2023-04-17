class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int ec) {
        int mx=0;
        int n=candies.size();
        for(auto v: candies){
            if(mx<v) mx=v;
        }
        vector<bool>ans(n,false);
        for(int i=0;i<n;++i){
            if(candies[i]+ec>=mx) ans[i]=true;
        }
        return ans;
    }
};