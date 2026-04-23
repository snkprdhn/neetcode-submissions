class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        components = n
        
        def find(i):
            while i != parent[i]:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        for i, j in edges:
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                parent[root_j] = root_i
                components -= 1
                
        return components