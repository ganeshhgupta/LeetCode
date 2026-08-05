class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        # O(n), O(1)
        # simulate one round of instructions
        # track position and direction
        # bounded if back to origin or direction changes

        x, y = 0, 0
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]  # N,E,S,W
        d = 0

        for ch in instructions:

            if ch == "G":
                dx, dy = dirs[d]
                x += dx
                y += dy

            elif ch == "L":
                d = (d - 1) % 4

            else:
                d = (d + 1) % 4

        return (x == 0 and y == 0) or d != 0