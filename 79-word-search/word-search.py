class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):

            if i == len(word):
            #which means we're at the last letter matching of the word which means we have found the word:
                return True

            if (r < 0 or c < 0 or           #exceeding left and top borders
                r >= rows or c >= cols or     #exceeding right and bottom borders
                word[i] != board[r][c] or   #incorrect letter match in next sequence
                (r, c) in path ):           #using the same exact letter on board twice
                return False

            #else, characters match, so add coords tuple to path set:
            path.add((r, c))

            #now recurse in all four directions and you're done
            res = (dfs(r + 1, c    , i + 1) or 
                   dfs(r - 1, c    , i + 1) or 
                   dfs(r,     c + 1, i + 1) or 
                   dfs(r,     c - 1, i + 1))

            #Without path.remove((r, c)), once you visit a cell, it would remain marked as "visited" forever, which would prevent the algorithm from trying that cell again in a different path search, even if it should be revisited in a different context
            #Unmarks the current cell after the recursive search from that cell is complete, allowing other paths to revisit it
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
