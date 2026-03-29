class Solution:
    def shortestPalindrome(self, s: str) -> str:

        # O(n), O(n)
        if not s:
            return s

        # build combined string
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

        # fail[-1] = length of longest palindromic prefix
        l = fail[-1]

        # suffix that is not part of the palindromic prefix
        suffix = s[l:]

        # prepend the reverse of that suffix
        return suffix[::-1] + s