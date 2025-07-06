class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = n * (n + 1) // 2
        count = n // m
        div_sum = m * (count * (count + 1) // 2)
        return res - 2 * div_sum
