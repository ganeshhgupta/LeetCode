class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]  # reversing

        # Pad the shorter string with '0's
        if len(a) < len(b):
            a += '0' * (len(b) - len(a))
        else:
            b += '0' * (len(a) - len(b))

        res = []
        carry = 0

        for i in range(len(a)):
            A = int(a[i])
            B = int(b[i])

            total = A + B + carry
            res.append(str(total % 2))
            carry = total // 2

        if carry:
            res.append('1')

        return ''.join(res[::-1])
