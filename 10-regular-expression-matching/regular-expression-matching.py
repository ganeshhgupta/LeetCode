class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # '*' matches 0 or any number of PRECEEDING element
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)] # p across cols, s across rows
        dp[0][0] = True

        # intialize first row
        # when we encounter '*', '*' and the char preceeding it can be skipped like they didn't even exist, 
        # since we skip two chars, so simply pick the last value two cells from left, dp[0][j-2]
        for j in range(2, n): 
                    if p[j-1] == '*':
                        dp[0][j] = dp[0][j-2]

        for i in range(1, m):
            for j in range(1, n):

                if p[j-1] == '.' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1] # top left diag

                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] # pick from 2 cells to left
                                          # cause dp[i][j-1]th char could be skipped, so pick last legit True?False value from dp[i][j-2]

                    if p[j-2] == '.' or p[j-2] == s[i-1]: # '.*' match any char any no. of times
                        dp[i][j] = dp[i][j] or dp[i-1][j] # keep as is or pick from top
        
        return dp[m-1][n-1]

                
'''
p  :  ∅  f  a  *  n  .  m
      0  1  2  3  4  5  6
    ┌──┬──┬──┬──┬──┬──┬──┬──┐
 ∅ 0│ T│ F│ F│ F│ F│ F│ F│
    ├──┼──┼──┼──┼──┼──┼──┼──┤
 f 1│ F│ T│ F│ T│ F│ F│ F│
    ├──┼──┼──┼──┼──┼──┼──┼──┤
 a 2│ F│ F│ T│ T│ F│ F│ F│
    ├──┼──┼──┼──┼──┼──┼──┼──┤
 a 3│ F│ F│ F│[T]│F│ F│ F│
    ├──┼──┼──┼──┼──┼──┼──┼──┤
 m 4│ F│ F│ F│ F│ T│ F│ F│
    ├──┼──┼──┼──┼──┼──┼──┼──┤
 a 5│ F│ F│ F│ F│ F│ T│ F│
    ├──┼──┼──┼──┼──┼──┼──┼──┤
 m 6│ F│ F│ F│ F│ F│ F│ T│
    └──┴──┴──┴──┴──┴──┴──┴──┘
'''