class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # O(n), O(1)
        n = len(graph)
        color = [-1] * n  # -1 = uncolored, 0 and 1 are the two colors
        
        # Handle all connected components
        for start in range(n):
            if color[start] != -1:  # Already colored
                continue
            
            # BFS using deque (similar to level order)
            q = collections.deque()
            q.append(start)
            color[start] = 0
            
            while q:
                node = q.popleft()
                
                # Process all neighbors (like processing children)
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        # Color with opposite color
                        color[neighbor] = 1 - color[node]
                        q.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # Conflict! Adjacent nodes have same color
                        return False
        
        return True