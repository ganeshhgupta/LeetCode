class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        # DFS + BT
        # 7^(n-1), O(7^n) with pruning due to memoization
        
        n = len(bottom)
        map = defaultdict(list)

        for a,b,c in allowed:
            map[ a + b ].append(c)
        
        s = set() # used rows

        def dfs(bottom, row, i): # curr bottom row, next row being constructed, i → current index in bottom
            n = len(bottom)

            if n == 1:
                return True # we reached the top

            if n == i: # curr bottom row covered, hence curr next row built
                if row in s:
                    return False
                
                s.add(row)
                return dfs(row, "", 1)

            pair = bottom[i-1] + bottom[i]

            for curr in map[pair]:
                if dfs(bottom, row + curr, 1 + i):
                    return True
            
            return False
        
        return dfs(bottom, "", 1)
        
