# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        s = root
        while s:
            root_val = s.val
            max_val = max(p.val, q.val)
            min_val = min(p.val, q.val)

            if min_val <= root_val and max_val >= root_val:
                return s
            
            if min_val < root_val:
                s = s.left
            else:
                s = s.right
            