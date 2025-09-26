class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        if (numerator < 0) ^ (denominator < 0):
            result.append('-')

        n, d = abs(numerator), abs(denominator)

        integer_part = n // d
        result.append(str(integer_part))

        remainder = n % d
        if remainder == 0:
            return ''.join(result)

        result.append('.')

        remainder_map = {}
        while remainder != 0:
            if remainder in remainder_map:
                idx = remainder_map[remainder]
                result.insert(idx, '(')
                result.append(')')
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // d))
            remainder %= d

        return ''.join(result)
