class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            if rank[pa] >= rank[pb]:
                parent[pb] = pa
                rank[pa] += rank[pb]
            else:
                parent[pa] = pb
                rank[pb] += rank[pa]

        # person 0 shares secret with firstPerson
        union(0, firstPerson)

        meetings.sort(key=lambda x: x[2])
        time_map = defaultdict(list)

        for x, y, t in meetings:
            time_map[t].append((x, y))

        for t in time_map:
            used = set()
            for x, y in time_map[t]:
                union(x, y)
                used.add(x)
                used.add(y)

            # rollback anyone not connected to 0
            for p in used:
                if find(p) != find(0):
                    parent[p] = p
                    rank[p] = 1

        root0 = find(0)
        return [i for i in range(n) if find(i) == root0]
