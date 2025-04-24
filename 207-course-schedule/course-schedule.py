from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #graph = {i: [] for i in range(numCourses)}
        graph = defaultdict(list)
        print(graph)
        for dest, src in prerequisites:
            graph[dest].append(src)
        
        print(graph)
        visited = [0] * numCourses
        
        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visited[course] = 2
            return True
        
        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):
                    return False
        
        return True
