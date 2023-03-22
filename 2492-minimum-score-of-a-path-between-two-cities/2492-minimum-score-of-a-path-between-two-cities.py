class Solution(object):
    def minScore(self, n, roads):
        v=set()
        def dfs(g,vis,s):
            if s in vis:
                return 
            vis.add(s)
            for i in g[s]:
                if i not in vis:
                    v.add(i)
                    dfs(g,vis,i)
            
            
        d={}
        for i in roads:
            d[(i[0],i[1])]=i[2]
        g=[[] for i in range(n+1)]
        for i in roads:
            g[i[0]].append(i[1])
            g[i[1]].append(i[0])
        vis=set()
        dfs(g,vis,1)
        ans=987654567898765
        for i in d.keys():
            if i[0] in v or i[1] in v:
                ans=min(ans,d[(i[0],i[1])])
        
        return ans
        
            
        