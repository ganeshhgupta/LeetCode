class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        # O(V + E), O(V + E)
        # https://www.youtube.com/watch?v=qrAub5z8FeA

        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        # tin: time of insertion (when DFS visited the node)
        # low: lowest tin reachable via back-edges in DFS tree

        tin = [0] * n
        low = [0] * n
        v = set()
        res = []
        self.timer = 1
        
        def dfs(node , par):

            v.add(node)
            tin[node] = low[node] = self.timer
            self.timer += 1
            
            for nei in adj[node]:
                if nei == par:
                    continue
                
                if nei not in v:
                    # Move to the next node
                    dfs(nei, node)
                    
                    # Upon return, update the low link of the current node
                    low[node] = min(low[node], low[nei])
                    
                    # Check if the edge is a bridge
                    if low[nei] > tin[node]:
                        res.append([node, nei])
                else:
                    # If already visited and not the parent, it's a back-edge
                    low[node] = min(low[node], tin[nei])

        # Start DFS from node 0
        dfs(0, -1)
        return res     