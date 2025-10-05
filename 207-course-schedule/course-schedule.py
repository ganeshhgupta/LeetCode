class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        v = set()
        adj = defaultdict(list)
        for c, pre in prerequisites:
            adj[c].append(pre)
        
        def cycleFree(c):
            if c in v: return False
            if adj[c] == [] : return True

            v.add(c)
            for pre in adj[c]:
                if not cycleFree(pre): return False

            v.remove(c)
            adj[c] = []
            return True
        
        for c in range(numCourses):
            if not cycleFree(c): return False
        return True
