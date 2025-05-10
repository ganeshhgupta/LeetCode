class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        map = Counter(s)
        
        odd_count = sum(1 for count in map.values() if count % 2 != 0)
        
        return odd_count <= 1
