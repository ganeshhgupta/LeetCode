class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        setA = set()
        res = 0

        for i in nums:
            if i not in setA:
                setA.add(i)
        l = len(setA)

        for j in range(len(nums)):
            setB = set()
            for i in range(j, len(nums)):
                setB.add(nums[i])
                if len(setB) == l:
                    res += 1
        
        return res