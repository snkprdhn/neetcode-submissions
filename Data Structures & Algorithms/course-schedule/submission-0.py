class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {}
        visited = set()

        for i in range(numCourses):
            pre_map[i] = []

        for i, j in prerequisites:
            pre_map[i].append(j)
        
        def dfs(course):
            if not pre_map[course]:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)
            for i in pre_map[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            pre_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True