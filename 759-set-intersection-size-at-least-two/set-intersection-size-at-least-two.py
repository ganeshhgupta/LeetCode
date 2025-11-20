class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[1], -x[0]))

        a = intervals[0][1] - 1
        b = intervals[0][1]
        count = 2  # we already picked {a, b}

        for start, end in intervals[1:]:
            # Case 1: interval already has at least two points
            if start <= a:
                continue
            
            # Case 2: interval has exactly one point (only b works)
            if start <= b:
                # need one more point
                a = b
                b = end
                count += 1
            else:
                # Case 3: interval has no points → need two new points
                a = end - 1
                b = end
                count += 2
        
        return count
