class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        # O(N + K), O(obs)
        curr_x, curr_y = 0, 0
        dir = 0  # 0: up, 1: right, 2: down, 3: left
        obs = set(map(tuple, obstacles))
        res = 0

        for i in commands:

            if i == -1:
                dir = (dir + 1) % 4
            elif i == -2:
                dir = (dir - 1) % 4
            
            else:
                steps = i
                while steps > 0:

                    # move ONE step at a time
                    if dir == 0:
                        nx, ny = curr_x, curr_y + 1
                    elif dir == 1:
                        nx, ny = curr_x + 1, curr_y
                    elif dir == 2:
                        nx, ny = curr_x, curr_y - 1
                    else:  # dir == 3
                        nx, ny = curr_x - 1, curr_y

                    # check obstacle BEFORE moving
                    if (nx, ny) in obs:
                        break

                    curr_x, curr_y = nx, ny

                    res = max(res, curr_x**2 + curr_y**2)

                    steps -= 1
        
        return res