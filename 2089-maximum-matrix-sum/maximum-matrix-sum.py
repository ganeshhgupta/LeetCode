class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        '''
        Sum absolute values of all numbers → this is the sum if all numbers were positive.

        Count negative numbers → if there’s an even number of negatives, you can flip them all to positive, so the total sum is just the absolute sum.

        If there’s an odd number of negatives, one negative will remain. To minimize the loss, subtract twice the smallest absolute value (flip the smallest number to negative).
        '''

        totalSum = 0
        neg = 0
        minAbs = float('inf')

        for row in matrix:
            for v in row:
                if v < 0:
                    neg += 1
                av = abs(v)
                totalSum += av
                minAbs = min(minAbs, av)

        return totalSum if neg % 2 == 0 else totalSum - 2 * minAbs   