class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        unq = set()

        for i in nums:
            if i in unq:
                unq.remove(i)
            else:
                unq.add(i)
        
        return unq.pop()
        