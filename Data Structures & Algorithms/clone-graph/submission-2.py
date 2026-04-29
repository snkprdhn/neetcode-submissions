"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        adj = {}

        def dfs(node):
            new_node = Node(node.val)
            adj[node] = new_node
            for nxt in node.neighbors:
                if nxt in adj:
                    new_node.neighbors.append(adj[nxt])
                else:
                    new_node.neighbors.append(dfs(nxt))
            
            return new_node
        
        return dfs(node)
        