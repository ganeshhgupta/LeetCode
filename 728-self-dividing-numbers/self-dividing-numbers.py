class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:

        res = []
        for i in range(left, right + 1):

            n = i
            flag = True

            while n > 0:
                rem = n % 10
                if rem == 0 or i % rem != 0:
                    flag = False
                    break
                n //= 10

            if flag:
                res.append(i)

        return res