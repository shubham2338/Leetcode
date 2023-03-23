class Solution(object):
    def makeConnected(self, n, connections):
        def dfs(i,vis,g):
            vis.add(i)
            for j in g[i]:
                if j not in vis:
                    vis.add(j)
                    dfs(j,vis,g)
        g=[[] for i in range(n+1)]
        for i in connections:
            g[i[0]].append(i[1])
            g[i[1]].append(i[0])
        vis=set()
        ans=-1
        c=0
        cab=len(connections)
        for i in range(n):
            if i not in vis:
                ans+=1
                dfs(i,vis,g)
            else:c+=1
        cab-=c
        if cab<ans:
            return -1
        return ans
        