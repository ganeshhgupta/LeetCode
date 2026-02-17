class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        # can brute force cause low constraint, loop with always run 12 x 60 times O(1)
        
        res = []
        
        for hour in range(12):
            for minute in range(60):

                if (bin(hour).count('1') + bin(minute).count('1')) == turnedOn:
                    res.append(f"{hour}:{minute:02d}")
        
        return res
