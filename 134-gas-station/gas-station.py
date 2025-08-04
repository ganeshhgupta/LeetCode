class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        c, g, t, s = 0, 0, 0, 0
        for i in range(len(gas)):
            g += gas[i]
            c += cost[i]
            t += gas[i] - cost[i]

            if t < 0:
                s = i + 1
                t = 0

        if g < c:
            return -1
        return s
