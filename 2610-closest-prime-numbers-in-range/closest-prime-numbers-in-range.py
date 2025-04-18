class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def getPrimes(left, right):

            li = [True] * (right + 1)
            li[0] = li[1]  = False

            for n in range(2, int(sqrt(right)) + 1):
                if not li[n]:
                    continue
                for m in range(n+n, right + 1, n):
                    li[m] = False
            primes = []
            for i in range(len(li)):
                if li[i] == True and i >= left :
                    primes.append(i)

            return primes

        primes = getPrimes(left, right)

        min_diff = float("inf")
        min_pair = [-1,-1]
        for i in range(len(primes) - 1):
            if primes[i+1] - primes[i] < min_diff:
                min_diff = primes[i+1] - primes[i]
                min_pair = [ primes[i],  primes[i+1]]
            
        return min_pair