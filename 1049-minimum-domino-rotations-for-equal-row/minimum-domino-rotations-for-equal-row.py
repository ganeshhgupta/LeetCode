class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        for x in [tops[0], bottoms[0]]:

            top_rotations = bottom_rotations = 0
            possible = True
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    possible = False
                    break
                if tops[i] != x:
                    top_rotations += 1
                if bottoms[i] != x:
                    bottom_rotations += 1
            if possible:
                return min(top_rotations, bottom_rotations)
        
        return -1
