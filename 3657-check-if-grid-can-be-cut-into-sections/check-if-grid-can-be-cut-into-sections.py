class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        horz, vert = [], []
        h_end, v_end = 0, 0
        h_count, v_count = 0, 0
        for startx, starty, endx, endy in rectangles:
            horz.append((startx, endx))
            vert.append((starty, endy))

        #print(horz, vert)
        horz = sorted(horz, key=lambda x: x[0])
        vert = sorted(vert, key=lambda x: x[0])
        #print(horz, vert)

        for i in range(len(rectangles)-1):
            #print(horz[i], horz[i+1])
            h_end, v_end = max(h_end, horz[i][1]), max(v_end, vert[i][1])
            if horz[i][1] <= horz[i+1][0] and horz[i+1][0] >= h_end:
                h_count += 1
            if vert[i][1] <= vert[i+1][0] and vert[i+1][0] >= v_end:
                v_count += 1
        #print(h_count, v_count)
        if max(h_count, v_count) >= 2:
            return True
        return False




