class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0 , len(matrix) - 1
        while l < r: 
            for i in range(r - l):
                top, bottom = l , r
                # Firstly store the topleft value in a temp variable
                topleft = matrix[top][l + i]

                # Move the bottom left to top left 
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move the Bottom Right to Bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move the Top right to bottom right 
                matrix[bottom][r - i] = matrix[top + i][r]

                #Move the top left value stored in temp to top right
                matrix[top + i][r] = topleft
            l += 1
            r -= 1