class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # O(mn), O(mn)
        # youtube.com/watch?v=mNbzDlGKmLs

        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)] # p across cols, s across rows
        dp[0][0] = True

        for j in range(2, n): 
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        print(dp)
        for i in range(1, m):
            for j in range(1, n):

                if p[j-1] in [s[i-1], '.' ]:
                    dp[i][j] = dp[i-1][j-1] # pick from top left diag

                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] # pick from two cells left

                    if p[j-2] in [ s[i-1], '.' ] : # if in a given row, the p[char] to the left of '*' matchs curr s[char]
                        dp[i][j] = dp[i][j] or dp[i-1][j] # pick from top
        print(dp)
        return dp[m-1][n-1]

'''
strings are 0-indexed:

s = a b b b c 	p = a b * c
    0 1 2 3 4	    0 1 2 3

dp is 1-indexed:
 	        0      1      2      3
        0 x    1 a    2 b    3 *    4 d
  0 x [[True, False, False, False, False], 
0 1 a [ False, True, False, True, False], 
1 2 b [ False, False, True, True, False], 
2 3 b [ False, False, False, True, False], 
3 4 b [ False, False, False, True, False], 
4 5 c [ False, False, False, False, True]]

'''