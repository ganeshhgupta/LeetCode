class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        # O(n), O(n)
        
        li = []  # store number of security devices per non-empty row

        for row in bank:
            count = row.count('1')
            if count > 0:
                li.append(count)
        
        res = 0
        for i in range(1, len(li)):
            res += li[i-1] * li[i]
        
        return res
