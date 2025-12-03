class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        MOD = 10 ** 9 + 7
        total_lines = 0
        res = 0

         # dict with (y coord : no. of points on that line)

        y_coords = defaultdict(int)

        for x, y in points:
            y_coords[y] += 1
        

        for y, point in y_coords.items():

            # can form nC2 lines from n points :
            curr_lines = point * (point - 1) // 2

            # just multiply no. of lines in current y-coord with all the other existing lines
            res = (res + total_lines * curr_lines) % MOD

            # and simple keep doing curr * total for all possible combinations
            total_lines = (total_lines + curr_lines) % MOD
        
        return res