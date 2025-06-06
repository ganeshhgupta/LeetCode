class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        l1, l2 = m - 1, n - 1
        l3 = m + n - 1

        while l2 >= 0 and l1 >= 0:
            if nums1[l1] > nums2[l2]:
                nums1[l3] = nums1[l1]
                l1 -= 1
            else:
                nums1[l3] = nums2[l2]
                l2 -= 1
            l3 -= 1

        while l2 >= 0:
            nums1[l3] = nums2[l2]
            l2 -= 1
            l3 -= 1

        print(nums1)      
