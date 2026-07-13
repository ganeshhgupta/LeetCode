class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        s = "123456789"
        res = []

        N, M = len(str(low)), len(str(high))

        for length in range(N, M + 1):

            for start in range(10 - length):

                num = int(s[start:start + length])

                if low <= num <= high:
                    res.append(num)

        return res