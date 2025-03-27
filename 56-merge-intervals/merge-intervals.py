class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        i = 0
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        while i <= len(sorted_intervals) - 2:
            #print(i)
            if sorted_intervals[i][1] >= sorted_intervals[i+1][0] :
                sorted_intervals.insert(i, [min(sorted_intervals[i][0],sorted_intervals[i+1][0]) , max(sorted_intervals[i+1][1], sorted_intervals[i][1] )]) 
                #print(sorted_intervals)
                sorted_intervals.pop(i+1)
                sorted_intervals.pop(i+1)                
                #print(sorted_intervals)
            else:
                i += 1
        
        return sorted_intervals