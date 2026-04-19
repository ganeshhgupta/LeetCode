class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        # O(n), O(1)
        l1, l2 = len(nums1), len(nums2)
        i, j = 0, 0
        res = 0

        while i < l1 and j < l2:
            if nums1[i] <= nums2[j]:
                res = max(res, j - i)
                j += 1
            else:
                i += 1

        return res