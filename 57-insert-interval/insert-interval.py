class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        if newInterval[1] <  intervals[0][0]:
            intervals.insert(0, newInterval) 
            print("here")
            return intervals

        if newInterval[0] >  intervals[len(intervals) - 1][1]:
            intervals.append(newInterval) 
            print("no, here")
            return intervals

        # ^ stupid corner cases

        # anyway, so for newInterval[0], check left to right, it would fall within an interval or outside bw two intervals, first occurence, then break
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                start = min(intervals[i][0], newInterval[0])
                start_index = i
                print("start: ", start, start_index)
                break

        # same for newInterval[1], right to left
        for i in range(len(intervals) - 1, -1, -1):
            if intervals[i][0] <= newInterval[1]:
                end = max(intervals[i][1], newInterval[1])
                end_index = i
                print("end: ", end, end_index)
                break

        print(start, end)
                
        n = len(intervals) - 1
        print(n )
        print(start_index, end_index + 1)
        for i in range(start_index, end_index + 1) :
            intervals.pop(start_index)
        print(intervals)
        intervals.insert(start_index, [start, end])    

        print(intervals)
        return intervals