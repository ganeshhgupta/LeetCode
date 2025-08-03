class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        res = 0
        for n, u in boxTypes:
            if truckSize == 0:
                break

            boxes_to_take = min(truckSize, n)
            res += boxes_to_take * u
            truckSize -= boxes_to_take

        return res
