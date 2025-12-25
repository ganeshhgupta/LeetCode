class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        h = sorted(happiness, reverse=True)
        res = 0
        sadness = 0
        
        for i in h:
            if sadness == k:
                break
            res += max(0, i - sadness)
            sadness += 1
        
        return res
