# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, i, p):
        def search(arr,st,end,val):
            for i in range(st,end+1):
                if arr[i]==val:
                    break
            return i
        def bt(i,p,st,end,pi):
            if st>end: return None
            node=TreeNode(p[pi[0]])
            pi[0]-=1
            if st==end:
                return node
            ind=search(i,st,end,node.val)
            node.right=bt(i,p,ind+1,end,pi)
            node.left=bt(i,p,st,ind-1,pi)
            
            return node
        pi=[len(p)-1]
        n=len(p)-1
        return bt(i,p,0,n,pi)
        