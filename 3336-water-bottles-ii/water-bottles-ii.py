class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empty = 0
        
        while numBottles > 0:
            # drink all current bottles
            res += numBottles
            empty += numBottles
            numBottles = 0
            
            # try exchanging while possible
            if empty >= numExchange:
                empty -= numExchange
                numBottles += 1
                numExchange += 1
            else:
                break
        
        return res
