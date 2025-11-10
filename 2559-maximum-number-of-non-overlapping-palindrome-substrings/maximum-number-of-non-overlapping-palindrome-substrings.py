class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        res = 0
        n = len(s)
        last_end = -1  # end index of the last selected palindrome
        
        for i in range(n):
            # odd-length palindromes
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k and l > last_end:
                    res += 1
                    last_end = r
                    break  # take the first valid palindrome starting at i
                l -= 1
                r += 1
            
            # even-length palindromes
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k and l > last_end:
                    res += 1
                    last_end = r
                    break  # take the first valid palindrome starting at i
                l -= 1
                r += 1
        
        return res
