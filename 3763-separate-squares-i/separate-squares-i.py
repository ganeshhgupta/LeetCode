class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        # O(n log n), O(n) n:Sqaures
        A = sum((l * l for x, y, l in squares))
        strips = [(y, 1, l) for x, y, l in squares] + [(y + l, 0, l) for x, y, l in squares]
        # (y, 1, l) here 1 -> start of sqaure, (y + l, 0, l) 0 -> end
        strips.sort()
        width = curr_a = prev_h = 0

        for i in range(len(strips)):
            y, start, l = strips[i]
            h_diff = y - prev_h
            a_diff = width * h_diff

            if curr_a + a_diff >= A / 2:
                req_h = (A / 2 - curr_a) / width
                return prev_h + req_h
            
            width += l if start == 1 else -l
            curr_a += a_diff
            prev_h = y