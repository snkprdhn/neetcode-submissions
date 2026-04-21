# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_sum = float("-inf")
        def find_sum(node):
            left_sum = 0
            right_sum = 0
            if node.left:
                left_sum = find_sum(node.left)
            if node.right:
                right_sum = find_sum(node.right)
            cur_val = node.val

            max_path = max(left_sum+cur_val, right_sum+cur_val)
            total_sum = left_sum + right_sum + cur_val
            self.max_sum = max(self.max_sum, max_path, total_sum, cur_val)
            return max(max_path, cur_val)
        
        find_sum(root)
        return self.max_sum
