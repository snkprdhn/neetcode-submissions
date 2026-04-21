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
            # def traverse(node, l):
            #     if len(self.res)>=l:
            #         self.res[l-1].append(node.val)
            #     else:
            #         self.res.append([node.val])
                
            #     if node.left:
            #         traverse(node.left, l+1)
            #     if node.right:
            #         traverse(node.right, l+1)
            
            # traverse(root, 1)

            s = [[root, 1]]
            while s:
                node, level = s.pop()
                if len(self.res)>=level:
                    self.res[level-1].append(node.val)
                else:
                    self.res.append([node.val])
                if node.right:
                    s.append([node.right, level+1])
                if node.left:
                    s.append([node.left, level+1])


        return self.res