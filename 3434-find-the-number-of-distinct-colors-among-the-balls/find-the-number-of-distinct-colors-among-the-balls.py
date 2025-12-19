class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        ball = {}                     # ball -> color
        colorCount = defaultdict(int) # color -> frequency
        res = []

        for x, y in queries:
            if x in ball:
                old = ball[x]
                colorCount[old] -= 1
                if colorCount[old] == 0:
                    del colorCount[old]

            ball[x] = y
            colorCount[y] += 1
            res.append(len(colorCount))

        return res
