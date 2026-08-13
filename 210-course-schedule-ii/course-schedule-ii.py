class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # KAHN's: O(V + E), O(V + E)
        # Courses with no prerequisites have indegree = 0.
        # Start BFS with those courses, then decrease indegree of neighbors.

        adj = defaultdict(list)
        indegree = [0] * numCourses
        res = []

        for c, prereq in prerequisites:
            adj[prereq].append(c)
            indegree[c] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                res.append(i)

        count = 0

        while q:
            course = q.popleft()
            count += 1

            for nei in adj[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
                    res.append(nei)

        return res if count == numCourses else []