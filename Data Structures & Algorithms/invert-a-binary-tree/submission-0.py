# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert_tree(self, root):
        if not root:
            return
        
        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root
        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert_tree(root)
        