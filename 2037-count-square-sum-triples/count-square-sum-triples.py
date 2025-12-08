class Solution:
    def countTriples(self, n: int) -> int:

        res = 0
        for a in range(1, n):
            for b in range(a + 1, n):

                c_squared = a * a + b * b
                c = int(c_squared ** 0.5)
                
                if c * c == c_squared and c <= n:
                    res += 2 # count both (a, b, c) and (b, a, c)
        return res
