# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        q=collections.deque()
        q.append((root,-float('inf')))
        while q:
            lenq=len(q)
            for i in range(len(q)):
                node,max_val=q.popleft()
                if node:
                    if node.val>=max_val:
                        count=count+1
                        max_val=node.val
                    q.append((node.left,max_val))
                    q.append((node.right,max_val))
        return count
                
                



