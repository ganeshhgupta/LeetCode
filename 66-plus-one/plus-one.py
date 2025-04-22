class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] + carry > 9:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
                    break
            else:
                 digits[i] =  digits[i] + carry
                 carry = 0
                 
        return digits
