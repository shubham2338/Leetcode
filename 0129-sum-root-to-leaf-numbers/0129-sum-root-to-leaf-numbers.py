# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def dfs(root,v):
            if root is None:
                return 0
            if not root.left and not root.right:
                v=v*10+root.val
                ans[0]+=v
            dfs(root.left,v*10+root.val)
            dfs(root.right,v*10+root.val)
        dfs(root,0)
        return ans[0]
        