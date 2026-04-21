# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.is_found = False

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p and q:
                if p.val != q.val:
                    return False
            
            if (p and not q) or (q and not p):
                return False
            
            if not p and not q:
                return True
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right) 

        # def check_tree(n1, n2):
        #     if n1.val == n2.val:
        #         if not n2.left and not n2.right and not n1.left and not n1.right:
        #             print(n1.val, n2.val)
        #             self.is_found = True
        #             return
        #         if n1.left and n2.left:
        #             check_tree(n1.left, n2.left)
        #         if n1.right and n2.right:
        #             check_tree(n1.right, n2.right)
        #     else:
        #         return

        def helper(n1, n2):
            if n1.val == n2.val:
                self.is_found = isSameTree(n1, n2)
            if not self.is_found:
                if n1.left:
                    helper(n1.left, n2)
                if n1.right:
                    helper(n1.right, n2)
            
        helper(root, subRoot)
        
        return self.is_found
