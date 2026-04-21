class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {}
        visited = set()
        res = []

        for course in range(numCourses):
            pre_map[course] = []
        
        for course, pre in prerequisites:
            pre_map[course].append(pre)
        
        def dfs(course):
            if not pre_map[course]:
                if not course in res:
                    res.append(course)
                return True
            
            if course in visited:
                return False
            
            visited.add(course)
            for i in pre_map[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            pre_map[course] = []
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res