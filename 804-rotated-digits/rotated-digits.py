class Solution:
    def rotatedDigits(self, n: int) -> int:

        # O(n⋅d), O(d), d = log n
        
        count = 0

        for num in range(1, n + 1):
            s = str(num)

            if '3' not in s and '4' not in s and '7' not in s:
                if '2' in s or '5' in s or '6' in s or '9' in s:
                    count += 1

        return count