class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        count = 0
        numset = set()
        for p in itertools.permutations(digits, 3):
            numset.add(p)

        print(numset)
        for p in numset:
            if p[-1] % 2 == 0 and (p[-2] != 0 or ( p[-2] != 0 and p[-3] == 0)):
                count += 1

        return count