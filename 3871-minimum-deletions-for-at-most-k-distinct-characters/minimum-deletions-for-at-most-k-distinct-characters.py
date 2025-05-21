class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        from collections import Counter

        freq = Counter(s)
        if len(freq) <= k:
            return 0

        counts = sorted(freq.values())
        excess = len(counts) - k
        deletions = 0

        for i in range(excess):
            deletions += counts[i]

        return deletions
