class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # O(E log E), O(E)
        # Hierholzer's algorithm, not ordinary DFS

        # Always take the smallest available destination first.
        # If we get stuck before using all tickets, backtrack and place that airport later.
        # An airport is added to the answer only when it has no unused outgoing ticket.
        # Reverse the result because airports are added in postorder.

        graph = defaultdict(list)

        for a, b in tickets:
            graph[a].append(b)

        for src in graph:
            graph[src].sort(reverse=True)

        res = []

        def dfs(src):
            while graph[src]:
                dst = graph[src].pop()
                dfs(dst)

            res.append(src)

        dfs("JFK")

        return res[::-1]