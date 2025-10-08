class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # O(n+q), O(n+q) , n:array len, q:query len

        # Step 1: Precompute rightmost reachable index
        rightmost = [0] * n
        rightmost[0] = 0
        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                rightmost[i] = rightmost[i-1]  # extend previous segment
            else:
                rightmost[i] = i  # new segment starts

        #print(rightmost)
        
        # Step 2: Answer queries
        res = []
        for u, v in queries:
            # ensure u <= v
            if u > v:
                u, v = v, u
            # v is reachable from u if rightmost[v] <= u or rightmost[u] >= v
            res.append(rightmost[v] <= u or rightmost[u] >= v)
        
        return res
