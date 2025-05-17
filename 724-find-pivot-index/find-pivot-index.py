class Solution:
    def pivotIndex(self, nums):

        rs = sum(nums)
        ls = 0
        for index, i in enumerate(nums):
            rs -= i
            if ls == rs:
                return index
            ls += i
        return -1