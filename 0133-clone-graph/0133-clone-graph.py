"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node,copy,vis):
            vis[copy.val]=copy
            for v in node.neighbors:
                if v.val not in vis:
                    h=Node(v.val)
                    copy.neighbors.append(h)
                    dfs(v,h,vis)
                else:
                    copy.neighbors.append(vis[v.val])
        if node is None: return
        vis={}
        copy=Node(node.val)
        dfs(node,copy,vis)
        return copy