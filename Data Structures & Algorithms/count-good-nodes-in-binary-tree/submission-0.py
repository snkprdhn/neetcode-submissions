# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        if root:
            s = [[root, root.val]]
            while s:
                node, max_val = s.pop()
                if node.val >= max_val:
                    good_nodes += 1
                
                cur_max_val = max(max_val, node.val)
                if node.right:
                    s.append([node.right, cur_max_val])
                if node.left:
                    s.append([node.left, cur_max_val])

        return good_nodes