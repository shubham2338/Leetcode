class Solution {
public:
    int partitionString(string s) {
        int i=0,res=1;
        set<char>h;
        for(i=0;i<s.length();i++){
            if(h.find(s[i])!=h.end()){
                res++;
                h.clear();
            }
            h.insert(s[i]);
        }
        return res;
    }
};