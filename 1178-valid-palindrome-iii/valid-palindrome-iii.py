class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = {}

        def pal(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            while i < j:
                if s[i] != s[j]:
                    if k == 0:
                        memo[(i, j, k)] = False
                        return False
                    res = pal(i + 1, j, k - 1) or pal(i, j - 1, k - 1)
                    memo[(i, j, k)] = res
                    return res
                i += 1
                j -= 1

            memo[(i, j, k)] = True
            return True

        return pal(0, len(s) - 1, k)
