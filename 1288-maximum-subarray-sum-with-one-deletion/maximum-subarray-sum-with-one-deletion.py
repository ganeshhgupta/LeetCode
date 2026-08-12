class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        # O(n), O(1)
        
        # Kadane's
        # noDel  → best subarray sum ending here WITHOUT deleting anything.
        # oneDel → best subarray sum ending here AFTER deleting exactly one element.

        noDel = oneDel = res = arr[0]

        for n in arr[1:]:

            oneDel = max(noDel, oneDel + n)
            noDel = max(n, noDel + n)

            res = max(res, noDel, oneDel)

        return res