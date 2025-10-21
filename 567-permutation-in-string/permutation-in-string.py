class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # O(n), O(1)
        
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)]) 

        if s1_count == s2_count:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            s2_count[ s2[r] ] += 1
            s2_count[ s2[l] ] -= 1

            if s2_count[ s2[l] ] == 0 :
                del s2_count[ s2[l] ]

            l += 1

            if s1_count == s2_count:
                return True
        
        return False