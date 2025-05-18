class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] + c > 9:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
                    break
            else:
                digits[i] = digits[i] + c
                c = 0
        return digits