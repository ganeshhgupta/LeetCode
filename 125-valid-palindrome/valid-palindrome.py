class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = list(s.lower())
        l = len(s) - 1
        while l > -1:
            if not (('a' <= s[l] <= 'z') or ('0' <= s[l] <= '9')):
                s.pop(l)
            l -= 1
        print(s)
        
        for i in range(0, (len(s) // 2)):
            print(s[i], s[len(s) - i - 1])
            if s[i] != s[len(s) - i - 1]:
                return False

        return True

        '''
        r a c e c a r
        0 1 2 3 4 5 6
        '''
