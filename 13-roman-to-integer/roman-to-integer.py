class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]: #use [] to access dictionary values
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        
        total += roman[s[-1]]  #last character

        return total
