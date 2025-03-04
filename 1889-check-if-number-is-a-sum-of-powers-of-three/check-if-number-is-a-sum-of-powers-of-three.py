class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        #helllo hello hello :')
        #anyways

        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

