# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid = True
        if root:
            s = [[root, float("inf"), float("-inf")]]
            while s:
                node, max_val, min_val = s.pop()
                print(node.val, max_val, min_val)
                if not (min_val < node.val < max_val):
                    return False

                if node.right:
                    s.append([node.right, max_val, node.val])
                if node.left:
                    s.append([node.left, node.val, min_val])
        return True