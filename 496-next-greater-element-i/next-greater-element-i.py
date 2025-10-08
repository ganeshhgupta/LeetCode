class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nxt_g = {}
        s = []

        for n in reversed(nums2):
            while s and s[-1] <= n:
                s.pop()
            nxt_g[n] = -1 if not s else s[-1]
            s.append(n)
        
        return [nxt_g[n] for n in nums1]