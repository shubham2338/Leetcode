class Solution(object):
    def countPairs(self, n, edges):
        c=[0]
        def dfs(i,vis,g):
            vis.add(i)
            c[0]+=1
            for adj in g[i]:
                if adj not in vis:
                    dfs(adj,vis,g)
            return c[0]            
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
                cnt=cnt-ans
                res+=(cnt*ans)
                c[0]=0
                
        return res
            