# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.is_bal = True

        def bal(node):
            if not node or not self.is_bal:
                return 0
            
            left_h = bal(node.left)
            right_h = bal(node.right)

            if abs(left_h-right_h) > 1:
                self.is_bal = False
            return 1 + max(left_h, right_h)
        bal(root)
        return self.is_bal