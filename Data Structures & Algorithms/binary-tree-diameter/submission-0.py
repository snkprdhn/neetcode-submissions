# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_d = 0
    def get_dia(self, node):
        if not node:
            return 0
        left_d = self.get_dia(node.left)
        right_d = self.get_dia(node.right)
        d = left_d+right_d
        self.max_d = max(d, self.max_d)
        return 1 + max(left_d, right_d)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_dia(root)
        return self.max_d