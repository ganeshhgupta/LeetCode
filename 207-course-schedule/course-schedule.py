class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # KAHN's O(V + E), O(V + E)
        # create graph, courses with no prereq are indegree = 1
        # start bfs with all indegree == 1 nodes, then do indegree -=1 for neis
        
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for c, prereq in prerequisites:
            adj[prereq].append(c)
            indegree[c] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0

        while q:
            course = q.popleft()
            count += 1

            for nei in adj[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return count == numCourses