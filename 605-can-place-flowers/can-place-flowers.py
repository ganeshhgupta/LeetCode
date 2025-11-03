class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # O(n), O(n)
        
        l = len(flowerbed)
        res = 0
        
        # edge
        if l == 1:
            if flowerbed[0] == 1:
                return False if n > 0 else True
            else:
                return True if n <= 1 else False

        if flowerbed[1] == 0 and flowerbed[0] == 0:
            flowerbed[0] = 1
            res +=1 
        
        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
            flowerbed[-1] = 1
            res += 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                res += 1

        return res >= n
        

