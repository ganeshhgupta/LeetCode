class Solution:
    def canWinNim(self, n: int) -> bool:
        
        '''
        Case I: n = 1 to 3
        whoever goes first wins.

        Case II: n = 4
        whoever goes first loses.

        Case III:
        n : 5 - 7 (whoever goes first tries to reach to n = 4, so Case II happens with the other person )
        
        so whoever start with n % 4 != 0 , wins
        '''

        return n % 4 != 0