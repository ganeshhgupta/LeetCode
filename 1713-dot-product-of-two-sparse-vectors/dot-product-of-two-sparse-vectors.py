class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []

        for i, nums in enumerate(nums):
            if nums:
                self.nums.append((i, nums))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:

        dot_product = 0
        i = j = 0

        while i < len(self.nums) and j < len(vec.nums):
            si, sval = self.nums[i]
            vj, vval = vec.nums[j]

            if si == vj:
                dot_product += sval * vval
                i += 1
                j += 1
                
            elif si > vj:
                j += 1
            else:
                i += 1
        
        return dot_product


        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)