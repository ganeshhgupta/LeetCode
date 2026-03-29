class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        # O(n), O(n)
        # idea: you can shuffle all even chars only within even indices and vice versa
        if len(s1) != len(s2):
            return False

        s1e = [0] * 26
        s1o = [0] * 26
        s2e = [0] * 26
        s2o = [0] * 26
        
        for i in range(len(s1)):
            if i % 2 == 1:  # odd
                s1o[ord(s1[i]) - 97] += 1
                s2o[ord(s2[i]) - 97] += 1
            else:
                s1e[ord(s1[i]) - 97] += 1
                s2e[ord(s2[i]) - 97] += 1
        
        return s1e == s2e and s1o == s2o