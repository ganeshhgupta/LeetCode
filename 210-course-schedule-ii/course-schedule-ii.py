class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        #list comp: map course to prerequisites
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet, cycleSet = set(), set()
        def dfs(crs):
            if crs in cycleSet:
                return False
            if crs in visitSet:
                return True

            cycleSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False

            cycleSet.remove(crs)
            visitSet.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
        return res

