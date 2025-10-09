class Solution:
    def candy(self, ratings: List[int]) -> int:

        # O(n), O(n)
        n = len(ratings)
        candies = [1] * n
        
        # Left to Right 1st Pass
        for i in range(1,n): # kids with a higher than their left neighbor get +1 candy
            if ratings[i] > ratings[i-1]: candies[i] = candies[i-1]+1
        
        # Right to Left 2nd Pass
        for i in range(n-2,-1,-1): # kids with a higher than their right neighbor get +1 candy
            if ratings[i] > ratings[i+1]: candies[i] = max(candies[i], candies[i+1]+1)
        
        return sum(candies)