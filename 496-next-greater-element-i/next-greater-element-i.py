class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # O(n), O(n)

        st = []
        res = []
        map = defaultdict(lambda: -1) # {val : next greatest val}

        for n in nums2:

            while st and st[-1] < n:
                val = st.pop()
                map[val] = n # n = next greatest val

            st.append(n)

        for n in nums1:
            res.append(map[n])

        return res