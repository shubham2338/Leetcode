#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        int c=0; long long s=987654345678;
        long long res=0;
        int n=matrix.size();
        for(int i=0;i<n;++i)
            for(int j=0;j<n;++j){
                int r=matrix[i][j];
                s=min(s,(long long)abs(r));
                if(r<0)c++;
                res+=abs(r);
            }
        if(c%2==0) return res;
        return res-(s*2);
    }
};