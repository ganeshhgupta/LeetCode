class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        # O(n), O(1)
        res = 0
        for i in operations:
            if i[1] == '+': res += 1
            else: res -= 1
        return res