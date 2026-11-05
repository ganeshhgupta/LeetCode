class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        
        res = 0

        for a1 in arr1:
            valid = True

            for a2 in arr2:
                if abs(a1 - a2) <= d:
                    valid = False
                    break

            if valid:
                res += 1

        return res