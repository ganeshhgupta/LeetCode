class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        # O(n²), O(n)
        pos = defaultdict(list)
        
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        res = float('inf')
        
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            for i in range(len(indices) - 2):
                dist = 2 * (indices[i+2] - indices[i])
                res = min(res, dist)
        
        return res if res != float('inf') else -1