# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        if root:
            s = [[root,1]]
            while s:
                node, l = s.pop()
                if len(self.res)>=l:
                    self.res[l-1].append(node.val)
                else:
                    self.res.append([node.val])
                
                if node.right:
                    s.append([node.right, l+1])
                if node.left:
                    s.append([node.left, l+1])

        return [val[-1] for val in self.res]


