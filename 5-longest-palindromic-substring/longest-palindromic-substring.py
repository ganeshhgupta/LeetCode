class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0

        def expand(l, r) -> int:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l-1, r+1
            return r - l - 1
        
        for i in range(len(s)):
            len1 = expand(i, i)       # Odd-length palindrome
            len2 = expand(i, i + 1)   # Even-length palindrome
            max_len = max(len1, len2)
            
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    

