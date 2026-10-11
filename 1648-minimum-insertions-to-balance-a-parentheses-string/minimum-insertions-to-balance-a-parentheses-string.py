class Solution:
    def minInsertions(self, s: str) -> int:

        # O(n), O(1)

        l, r = 0, len(s) - 1
        res = 0
        need = 0

        while l <= r:
            if s[l] == '(':
                need += 2

                if need % 2 == 1:
                    res += 1
                    need -= 1
            else:
                need -= 1

                if need < 0:
                    res += 1
                    need = 1

            l += 1

        return res + need