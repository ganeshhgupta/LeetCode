class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        evenMap = {}
        for i in nums:
            if i not in evenMap:
                evenMap[i] = 1
            else:
                evenMap[i] += 1

        for key , val in evenMap.items():
            if val % 2 != 0 :
                return False

        return True