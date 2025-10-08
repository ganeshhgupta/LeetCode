class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        # O(9^81), O(1)
        def isValid(b, r, c, v):
            for i in range(9):
                box_row = 3 * (r // 3) + i // 3 
                box_col = 3 * (c // 3) + i % 3
                
                if b[r][i] == v or b[i][c] == v or b[box_row][box_col] == v:
                    return False
            return True
        
        def solve(b):
            r_best, c_best, min_candidates = -1, -1, 10
            
            for r in range(9):
                for c in range(9):
                    if b[r][c] == '.':
                        
                        candidate_count = 0
                        for v in map(str, range(1, 10)):
                            if isValid(b, r, c, v):
                                candidate_count += 1
                        
                        if candidate_count < min_candidates:
                            min_candidates = candidate_count
                            r_best, c_best = r, c
                            if min_candidates == 0:
                                return False
            
            if r_best == -1:
                return True
            
            r, c = r_best, c_best
            
            for v in map(str, range(1, 10)):
                if isValid(b, r, c, v):
                    b[r][c] = v
                    if solve(b): 
                        return True
                    b[r][c] = '.'
                    
            return False

        solve(board)