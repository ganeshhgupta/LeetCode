class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        #separate the s and e in sorted arrays, 
        # if s < e, s++ c++ else e++ c--
        
        start = sorted([i for i, j in intervals])
        end = sorted([i for j, i in intervals])
        
        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if  start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e +=1
            res = max(res, count)

        return res