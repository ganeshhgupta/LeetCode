class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        # O(n), O(n)
        
        adj = defaultdict(list)
        for i, m in enumerate(manager):
            adj[m].append(i)

        q = deque([(headID, 0)])  # (employee, time)
        res = 0

        while q:
            id, time = q.popleft()
            res = max(res, time)

            for emp in adj[id]:
                q.append((emp, time + informTime[id]))

        return res