class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        
        # Separate numbers
        for n in nums:
            if n >= 0:
                pos.append(n)
            else:
                neg.append(n)
        
        res = [0] * len(nums)
        
        # Fill alternately
        i = 0
        for p, n in zip(pos, neg):
            res[i] = p
            res[i + 1] = n
            i += 2
        
        return res