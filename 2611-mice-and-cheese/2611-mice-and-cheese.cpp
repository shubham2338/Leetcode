class Solution {
public:
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        vector<pair<int,int>>indexes;
        for(int i=0;i<reward1.size();i++){
            indexes.push_back({reward1[i]-reward2[i],i});
        }
        sort(indexes.begin(),indexes.end());
        reverse(indexes.begin(),indexes.end());
        int r1=0,i;
        for(i=0;i<k;i++){
            auto x=indexes[i];
            int ind=x.second;
            r1+=reward1[ind];
        }
        
        for(;i<reward1.size();i++){
            auto x=indexes[i];
            int ind=x.second;
            r1+=reward2[ind];
        }
        return r1;
    }
    
};