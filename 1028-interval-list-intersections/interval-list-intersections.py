class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        if not firstList or not secondList:
            return []

        p1, p2 = 0, 0
        res = []
        while p1 < len(firstList) and p2 < len(secondList):

            s1, e1 = firstList[p1]
            s2, e2 = secondList[p2]

            if s1 > e2:
                p2 += 1
            elif s2 > e1:
                p1 += 1
            else:
                res.append([max(s1, s2), min(e1, e2)])

                if e1 > e2:
                    p2 += 1
                else:
                    p1 += 1

        return res