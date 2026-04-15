class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        if target not in words:
            return -1

        n = len(words)
        res = float('inf')
        
        for i, word in enumerate(words):
            if word == target:
                cur = abs(i - startIndex)
                res = min(res, cur, n - cur)
        
        return res