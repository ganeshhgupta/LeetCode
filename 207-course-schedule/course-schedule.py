class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for i, j in prerequisites:
            adj[i].append(j)
        
        v = set()

        def dfs(i):
            
            if i in v: return False
            if adj[i] == []: return True
            v.add(i)

            for j in adj[i]:
                if not dfs(j): return False
            
            v.remove(i)
            adj[i] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        
        return True
