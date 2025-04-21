class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        merged = []
        
        for i in intervals:
            #if merged is empty or no overlap, add curr interval as it is
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                #if overlap, merge the intervals by max(exisitng_end, new_end)
                merged[-1][1] = max(merged[-1][1], i[1])
        
        return merged
