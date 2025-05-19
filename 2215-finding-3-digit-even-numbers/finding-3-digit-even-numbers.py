class Solution:
    def findEvenNumbers(self, digits):
        from collections import Counter
        freq = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            og_num = num
            num = str(num)
            parts = [ int (num[0] ) , int( num[1]) , int(num[2]) ]
            count = Counter(parts)
            is_valid = True
            for d in count:
                if freq[d] < count[d]:
                    is_valid = False
                    break

            if is_valid:
                res.append(og_num)
        return res