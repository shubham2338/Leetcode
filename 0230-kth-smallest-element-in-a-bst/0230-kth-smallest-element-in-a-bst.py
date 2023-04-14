# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if root:
                h.append(root.val)
                dfs(root.left)
                dfs(root.right)
        h=[]
        dfs(root)
        h.sort()
        return h[k-1]