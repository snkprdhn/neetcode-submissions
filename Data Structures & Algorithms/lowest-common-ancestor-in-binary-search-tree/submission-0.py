# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        s = [root]
        while s:
            root = s.pop()
            root_val = root.val
            max_val = max(p.val, q.val)
            min_val = min(p.val, q.val)

            if min_val <= root_val and max_val >= root_val:
                return root
            
            if min_val < root_val:
                s.append(root.left)
            else:
                s.append(root.right)
            