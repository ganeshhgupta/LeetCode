class TrieNode:
    def __init__(self):
        self.ch = {}
        self.endOfWord = False

    def addWord(self, word: str) -> None:
        cur = self

        for c in word:
            if c not in cur.ch:
                cur.ch[c] = TrieNode()
            cur = cur.ch[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for w in words:
            root.addWord(w)

        N, M = len(board), len(board[0])
        dir = [[0,1], [1,0], [-1,0], [0,-1]]
        res, v = set(), set()

        def invalid(r, c, node):
            if not (0 <= r < N) or not (0 <= c < M) or (r, c) in v or board[r][c] not in node.ch:
                return True
            return False

        def dfs(r, c, node, w):
            if invalid(r, c, node): 
                return

            v.add((r, c))
            node = node.ch[board[r][c]]
            w += board[r][c]

            if node.endOfWord:
                res.add(w)
            
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, node, w)
            
            v.remove((r, c))
        
        for i in range(N):
            for j in range(M):
                dfs(i, j, root, "")
        
        return list(res)