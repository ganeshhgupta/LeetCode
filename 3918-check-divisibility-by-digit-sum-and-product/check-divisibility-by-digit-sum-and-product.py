class Solution:
    def checkDivisibility(self, n: int) -> bool:

        digits = [int(i) for i in str(n)]

        s = sum(digits)
        p = prod(digits)

        return n % (s + p) == 0