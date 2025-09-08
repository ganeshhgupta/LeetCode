class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        t = 0
        for i in range(n):
            t = n - i
            if '0' not in str(t) and '0' not in str(i):
                return [t, i]