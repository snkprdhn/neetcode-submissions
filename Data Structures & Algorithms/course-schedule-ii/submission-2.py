class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {}
        visited = set()
        res = []
        indegree = {}

        for course in range(numCourses):
            pre_map[course] = set()
            indegree[course] = 0
        
        for course, pre in prerequisites:
            if pre in pre_map[course]:
                return []
                
            pre_map[pre].add(course)
            indegree[course] += 1
            
        
        res = []
        q = deque()
        for course, degree in indegree.items():
            if not degree:
                q.append(course)
        
        print(pre_map)
        print(indegree)
        
        while q:
            course = q.popleft()
            res.append(course)
            for pre in pre_map[course]:
                indegree[pre] -= 1
                if not indegree[pre]:
                    q.append(pre)
        
        if len(res) != numCourses:
            return []
        return res
