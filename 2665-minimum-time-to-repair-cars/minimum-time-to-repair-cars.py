class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def count_repaired(mid):
            count = 0
            for r in ranks:
                count += int(sqrt(mid/r))
            return count


        l, r = 1, ranks[0] * cars * cars
        res = -1

        while l <= r:
            mid = (l + r ) // 2
            repaired = count_repaired(mid)
            if repaired >= cars:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        
        return res