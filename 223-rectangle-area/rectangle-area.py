class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        # O(1), O(1)
        
        cx1, cx2 = max(ax1, bx1), min(ax2, bx2)
        cy1, cy2 = max(ay1, by1), min(ay2, by2)

        overlap = 0
        if cx1 < cx2 and cy1 < cy2:
            overlap = (cx2 - cx1) * (cy2 - cy1)

        ra = (ax2 - ax1) * (ay2 - ay1)
        rb = (bx2 - bx1) * (by2 - by1)

        return ra + rb - overlap
