class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def consecutive_line_segments(bars):
            res = cnt = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    cnt += 1
                else:
                    cnt = 1
                if cnt > res: 
                    res = cnt
            return res

        return (min(consecutive_line_segments(sorted(vBars)), consecutive_line_segments(sorted(hBars))) + 1) ** 2