class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        s = strs[0]
        pre = ''
        for i in range(len(s)):
            for word in strs:
                if i >= len(word) or s[i] != word[i]:
                    return pre
            pre += s[i]
        return pre