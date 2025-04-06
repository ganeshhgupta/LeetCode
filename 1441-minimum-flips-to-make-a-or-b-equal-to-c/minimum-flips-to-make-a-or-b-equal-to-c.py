class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        a = list(bin(a))[2:]
        b = list(bin(b))[2:]
        c = list(bin(c))[2:]

        max_len = max(len(a), len(b), len(c))
        count = 0

        for i in range(max_len - len(a)):
            a.insert(0, '0')
        for i in range(max_len - len(b)):
            b.insert(0, '0')
        for i in range(max_len - len(c)):
            c.insert(0, '0')

        for i in range(len(c)):
            if int(a[i]) | int(b[i]) !=  int(c[i]):
                count += abs(int(a[i]) + int(b[i]) - int(c[i]))

        return count
