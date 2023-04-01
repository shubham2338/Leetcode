class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        ans=[9876543242]
        def dfs(i,vis,g,p,c):
            vis[i]=c
            for adj in g[i]:
                if adj==p: continue
                if vis[adj]!=98765:
                    ans[0]=min(ans[0],abs(vis[adj]-vis[i])+1)
                    continue
                dfs(adj,vis,g,i,c+1)
            return 
        g=[[] for i in range(n)]
        for i in edges:
            g[i[0]].append(i[1])
            g[i[1]].append(i[0])
        
        for i in range(n):
            vis=[98765]*(n)
            dfs(i,vis,g,-1,0)
        if ans[0]==9876543242:
            return -1
        return ans[0]
        