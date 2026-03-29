class Solution:
    def shortestPalindrome(self, s: str) -> str:

        # O(n), O(n) KMP array of s + '#' + rev(s)
        if not s:
            return s

        combined = s + '#' + s[::-1]

        # build KMP failure function
        fail = [0] * len(combined)
        j = 0
        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = fail[j - 1]
            if combined[i] == combined[j]:
                j += 1
            fail[i] = j

        l = fail[-1]
        suffix = s[l:]
        return suffix[::-1] + s