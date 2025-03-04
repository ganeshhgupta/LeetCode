class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]
        res = []
        curr = []

        #zeroth pass = [1, 2, 3]
        #first pass (first nested pass) = [2, 3]
        #sec pass = [3]
        #third pass = []
        #third pass ret = []
        #sec pass ret = [3] adding 3 in all possible indexes/spaces
        #first pass ret = [2,3], [3, 2] adding 2 in all possible indexes/spaces
        #zeroth pass ret = [1, 2, 3], [2, 1, 3], [2, 3, 1]   ,   [1, 3, 2], [3, 1, 2], [3, 2, 1] adding 1 in all possible indexes/spaces

        perms = self.permute(nums[1:])
        res = [] #store all possible lists of current pass (doesn't have to be size len(nums))

        for p in perms: #iterate through all lists in perms [[]]

            for i in range(len(p) + 1): #iterate through all possible indexes/spaces in p list
                p_copy = p.copy() #make a copy so doesn't write on the existing p list
                p_copy.insert(i, nums[0]) #insert the first element in nums (since in next self.permute(nums[1:]) we get rid of it )
                res.append(p_copy)

        return res
