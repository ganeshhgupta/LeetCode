class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # O(n), O(n)
        
        res = 0
        st = [] # (idx, height)

        for i, h in enumerate(heights):
            start = i

            while st and st[-1][1] > h: # if prev rec (st[-1]) > curr rec: keep popping and calc area
                idx, height = st.pop()
                res = max(res, height * (i - idx))
                start = idx # idx goes back
            
            st.append((start, h))
        
        # leftover stack elements:

        for i, h in st:
                res = max(res, h * (len(heights) - i))
        
        return res




