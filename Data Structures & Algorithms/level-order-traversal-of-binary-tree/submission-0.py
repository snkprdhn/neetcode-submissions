# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        if root:
            def traverse(node, l):
                if len(self.res)>=l:
                    self.res[l-1].append(node.val)
                else:
                    self.res.append([node.val])
                
                if node.left:
                    traverse(node.left, l+1)
                if node.right:
                    traverse(node.right, l+1)
                
            
            traverse(root, 1)

        return self.res