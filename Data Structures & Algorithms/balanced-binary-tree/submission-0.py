# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
  

        def dfs(curr):
            if curr is None:

                return 0
            lh=dfs(curr.left)
            lr=dfs(curr.right)
            if lh == -1 or lr == -1 or abs(lh-lr)>1:
                return -1
            else:
                return 1 + max(lh, lr)
        res=dfs(root)
        if res==-1:
            return False
        else:
            return True