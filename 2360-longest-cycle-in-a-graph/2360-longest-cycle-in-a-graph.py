class Solution(object):
    def longestCycle(self, edges):
        mx=[-1]
        def dfs(edges,i,vis,seen):
            if i not in seen:
                if i in vis:
                    mx[0]=max(mx[0],len(vis)-vis[i])
                elif edges[i]!=-1:
                    vis[i] = len(vis)
                    dfs(edges,edges[i],vis,seen)
                    vis.pop(i)
                seen[i]=True
    
        vis={}
        seen={}
        for i in edges:
            if i not in seen:
                dfs(edges,i,vis,seen)
        return mx[0]
        