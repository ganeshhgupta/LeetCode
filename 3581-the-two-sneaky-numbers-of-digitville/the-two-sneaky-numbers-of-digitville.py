class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums)
        res = []
        for k, v in c.items():
            if c[k] == 2:
                res.append(k)
        
        return res