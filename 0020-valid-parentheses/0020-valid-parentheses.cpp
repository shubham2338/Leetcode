class Solution {
public:
    bool isValid(string s) {
        stack<int>st;
        for(auto i:s){
            if(i=='(' || i=='{' || i=='[')st.push(i);
            else if((i==')' || i=='}' || i==']') && st.size()>0){
                if(i==')' && st.top()=='(') st.pop();
                else if(i=='}' && st.top()=='{') st.pop();
                else if(i==']' && st.top()=='[') st.pop();
                else st.push(i);
            }
            else st.push(i);
        }
        if (st.size()==0) return true;
        return false;
    }
};