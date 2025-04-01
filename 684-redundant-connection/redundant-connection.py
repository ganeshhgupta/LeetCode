class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        #union-find, union by rank, path-compression
        #list comprehension - [0, 1, 2, ...] #every component is their own parent
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n + 1) #size of each component

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2): #True if n1, n2 are disconnected components
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p2]

            return True

        for n1, n2 in edges:
            if not union(n1, n2): #if n1, n2 are connected: 
                return [n1, n2] #redundant edge
