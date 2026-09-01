class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # O(MN), O(M)
        N, M = len(text1), len(text2)

        prev = [0] * (M + 1)

        for i in range(N-1, -1, -1):

            curr = [0] * (M + 1)

            for j in range(M-1, -1, -1):

                # always curr[j] will be updated
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max( curr[j + 1], prev[j])
            
            prev = curr
        
        return prev[0]

