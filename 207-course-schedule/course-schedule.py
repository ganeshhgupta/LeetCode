class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        map = defaultdict(list)
        for c, pre in prerequisites:
            map[c].append(pre) # course:prereq adj list 
        
        def cycleFree(c): # dfs
            if c in visited: return False # same course encountered twice : loop
            if map[c] == []: return True # course has no prereqs : no loop
            
            visited.add(c)
            for pre in map[c]:
                if not cycleFree(pre): return False
                    
            visited.remove(c)
            map[c] = [] # we are done with this dfs path, so remove
            return True
        
        for c in range(numCourses):
            if not cycleFree(c):
                return False
        return True
