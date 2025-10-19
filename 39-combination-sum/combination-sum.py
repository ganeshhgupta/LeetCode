class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # O( 2^(target/min(candidates)) ) , O(number of solutions × avg length)
        res = []
        n = len(candidates)

        def dfs(i, li, cur):
            if i == n:
                if cur == target:
                    res.append(li.copy())
                return

            if cur > target or i == len(candidates):
                return
            
            dfs(i, li + [candidates[i]], cur + candidates[i])
            dfs(i + 1, li, cur)
            return
        
        dfs(0, [], 0)
        return res