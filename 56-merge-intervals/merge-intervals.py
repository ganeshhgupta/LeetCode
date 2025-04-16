class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        i = 0
        si = sorted(intervals, key=lambda x: x[0])
        while i <= len(si) - 2:
            curr, next, start, end = i, i+1, 0, 1
            if si[curr][end] >= si[next][start] :
                #expanding/merging i, i+1th interval if they overlap
                si.insert(i, [min(si[curr][start],si[next][start]) , max(si[next][end], si[curr][end] )]) 
                si.pop(i+1) #popping the two intervals which are now merged
                si.pop(i+1)                
            else:
                i += 1
        
        return si