class Solution:    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        for a in accounts:
            for email in a[1:]:
                graph[a[1]].add(email)
                graph[email].add(a[1])
        #print(graph.items())

        def dfs(node, visit):
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei, visit)
            self.res.append(node)
        
        visit = set()
        ans = []
        for a in accounts:
            name = a[0]
            for email in a[1:]:
                if email not in visit:
                    self.res = []
                    dfs(email, visit)
                    ans.append([name]+sorted(self.res))
        return ans