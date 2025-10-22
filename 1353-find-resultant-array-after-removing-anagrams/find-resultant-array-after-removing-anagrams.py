class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        st = []
        res = [words[0]]
        for w in words:
            c = [0] * 26
            for l in w:
                c[ord(l) - ord('a')] += 1
            if st and tuple(c) != st[-1]:
                res.append(w)
            st.append(tuple(c))
        
        return res