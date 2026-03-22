class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        # O(n^2), O(1)
        # rotate matrix problem
        
        def rotate(m):
            l, r = 0, len(m) - 1

            while l < r:
                for i in range(r - l):
                    t, b = l, r

                    topLeft = m[t][l + i]

                    m[t][l + i] = m[b - i][l]
                    m[b - i][l] = m[b][r - i]
                    m[b][r - i] = m[t + i][r]
                    m[t + i][r] = topLeft
                
                l += 1
                r -= 1

            return m

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)

        return False