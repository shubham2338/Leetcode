class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n=len(colors)
        g=defaultdict(list)
        ind=defaultdict(int)
        for u,v in edges:
            g[u].append(v)
            ind[v]+=1
        col=[ord(c)-ord('a') for c in colors]
        q=[]
        dp=[[0]*26 for i in range(n)]
        for u in range(n):
            if u not in ind:
                q.append(u)
                dp[u][col[u]]=1
        vis=0
        while q:
            u = q.pop()
            vis+=1
            for v in g[u]:
                for c in range(26):
                    dp[v][c]=max(dp[v][c],dp[u][c]+(c==col[v]))
                ind[v]-=1
                if ind[v]==0:
                    q.append(v)
                    del ind[v]
        if vis<n:
            return -1
        return max(max(x) for x in dp)
                    
            
        