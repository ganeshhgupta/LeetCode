class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        a, b, c = nums[0], nums[1], nums[2]

        if a == b == c:
            return "equilateral"
        
        if a + b > c and a + c > b and c + b > a:

            if a == b or b == c or c == a:
                return "isosceles"
            
            else:
                return "scalene"
        
        else:
            return "none"
