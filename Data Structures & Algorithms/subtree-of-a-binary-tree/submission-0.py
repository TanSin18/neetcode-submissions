# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)  

    def same(self, curr, p):
        if curr is None and p is None:
            return True
        elif curr and p and curr.val == p.val:
            return self.same(curr.left, p.left) and self.same(curr.right, p.right)
        else:
            return False