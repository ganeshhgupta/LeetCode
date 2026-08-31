class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        courses = [0] * numCourses

        for pre, course in prerequisites:
            adj[pre].append(course)
            courses[course] += 1

        q = deque()

        for c in range(numCourses):
            if courses[c] == 0:
                q.append(c)

        count = 0

        while q:

            course = q.popleft()
            count += 1

            for nei in adj[course]:
                courses[nei] -= 1

                if courses[nei] == 0:
                    q.append(nei)

        return count == numCourses