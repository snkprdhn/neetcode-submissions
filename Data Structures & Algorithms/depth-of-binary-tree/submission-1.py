# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, l, res):
        if not node:
            return
        if len(res) >= l:
            res[l-1].append(node.val)
        else:
            res.append([node.val])
        if node.left:
            self.dfs(node.left, l+1, res)
        if node.right:
            self.dfs(node.right, l+1, res)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            len_q = len(q)
            if len_q:
                depth += 1
            for _ in range(len_q):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth
        
            
        
            