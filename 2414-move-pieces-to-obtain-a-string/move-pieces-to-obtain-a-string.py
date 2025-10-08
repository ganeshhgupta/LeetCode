class Solution:
    def canChange(self, start: str, target: str) -> bool:

        # O(n), O(n)
        if start.replace('_', '') != target.replace('_', ''):
            return False  # sequence mismatch

        i = j = 0
        n = len(start)

        while i < n and j < n:
            while i < n and start[i] == '_': i += 1
            while j < n and target[j] == '_': j += 1

            if i == n and j == n: return True
            if i == n or j == n: return False

            if start[i] == 'L' and i < j: return False # L can only move left
            if start[i] == 'R' and i > j:  return False # R can only move right

            i += 1
            j += 1

        return True
