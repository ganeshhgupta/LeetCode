class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # O(N²), O(N)
        # to get [0, 1, .. n] 0th index stays unsed in both arrays, since input says 1-n

        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
    
        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p2] += rank[p1]
            else:
                par[p1] = p2
                rank[p1] += rank[p2]  
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return (n1, n2)
