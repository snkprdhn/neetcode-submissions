"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.c = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        
        def dfs(n1):
            if n1 in visited:
                return visited[n1]

            n2 = Node(n1.val)
            visited[n1] = n2
            for neighbor in n1.neighbors:
                n2.neighbors.append(dfs(neighbor))
            return n2

        return dfs(node)
            
            