from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        # O(n), O(n)
        
        c = Counter(nums)
        res = 0
        
        for num in c:
            comp = k - num 
            
            if num == comp:
                res += c[num] // 2

            elif comp in c:

                operations = min(c[num], c[comp])
                res += operations

                c[num] -= operations
                c[comp] -= operations
        
        return res
