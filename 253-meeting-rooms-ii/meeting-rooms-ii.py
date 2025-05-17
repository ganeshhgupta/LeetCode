class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        li = []
        for start, end in intervals:
            li.append([start, 1])
            li.append([end, -1])
        li.sort()
        
        curr = maxx = 0
        for time, change in li:
            curr += change
            maxx = max(maxx, curr)
        return maxx
