class Solution:
    def toHex(self, num: int) -> str:

        # O(n), O(1)
        
        if num == 0:
            return "0"

        # handle negative numbers (32-bit)
        num &= 0xffffffff
        
        res = ""

        def mod(n):
            letters = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
            m = n % 16
            if m > 9:
                return letters[m]
            else:
                return str(m)

        while num > 0:
            res = mod(num) + res
            num = num // 16

        return res
