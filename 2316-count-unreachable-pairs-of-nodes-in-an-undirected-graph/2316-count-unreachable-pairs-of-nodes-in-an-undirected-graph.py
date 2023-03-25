class Solution(object):
    def countPairs(self, n, edges):
        d=[0]
        def dfs(i,vis,g):
            vis.add(i)
            d[0]+=1
            for adj in g[i]:
                if adj not in vis:
                    dfs(adj,vis,g)
                    
            return d[0]
            
                
        g=[[] for i in range(n)]
        for i in edges:
            g[i[0]].append(i[1])
            g[i[1]].append(i[0])

        vis=set()
        cnt=n
        res=0
        for i in range(n):
            if i not in vis:
                ans=dfs(i,vis,g)
                d[0]=0
                cnt=cnt-ans
                res+=(cnt*ans)
                
        return res
            