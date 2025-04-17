class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                top_left = matrix[top][left + i] # save top_left to temp

                matrix[top][left + i] = matrix[bottom - i][left] #bl-tl
                matrix[bottom - i][left] = matrix[bottom][right - i] #br-bl
                matrix[bottom][right - i] = matrix[top + i][right] #tr-br
                matrix[top + i][right] = top_left #tl-tr(temp)
                
            left += 1
            right -= 1
            
