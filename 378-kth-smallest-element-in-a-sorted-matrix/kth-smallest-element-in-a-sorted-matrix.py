class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []

        # Initialize heap with first element from each row (first column of each row)
        for r in range(min(k, n)):  # no need to push more than k rows
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

        # Extract-min k times
        for _ in range(k):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

        return val
