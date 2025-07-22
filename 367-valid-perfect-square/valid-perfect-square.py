class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1 :
            return True
        start = 1
        end = num//2 + 1
        while start <= end :
            mid = start + (end-start)//2
            sqr = mid*mid
            if sqr == num :
                return True
            elif sqr < num:
                start = mid + 1
            else:
                end = mid - 1
        return False