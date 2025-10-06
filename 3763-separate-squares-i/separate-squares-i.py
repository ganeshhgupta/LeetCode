class Solution:      
    def separateSquares(self, squares: List[List[int]]) -> float:

        # O(n log(R)) n:Sqaure, R:Range, O(1)
        min_y = min(square[1] for square in squares)
        max_y = max(square[1] + square[2] for square in squares)
        precision = 1e-5

        def largerLow(squares, mid_y):
            la = 0
            ua = 0
            
            for s in squares:
                bottom_y = s[1]
                side = s[2]
                top_y = bottom_y + side
                
                if top_y <= mid_y:
                    la += side * side
                elif bottom_y >= mid_y:
                    ua += side * side
                else:
                    la += (mid_y - bottom_y) * side
                    ua += (top_y - mid_y) * side
            
            return la >= ua
        
        while max_y - min_y > precision:
            mid_y = (min_y + max_y) / 2
            if largerLow(squares, mid_y):
                max_y = mid_y
            else:
                min_y = mid_y
        
        return min_y