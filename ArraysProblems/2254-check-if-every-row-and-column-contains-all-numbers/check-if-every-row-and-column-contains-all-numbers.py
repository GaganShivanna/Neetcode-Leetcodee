class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        target = set(range(1, n + 1))

        for row in matrix:
            if set(row) != target:
                return False
        for col in range(n):
            col_val = set()
            for row in range(n):
                col_val.add(matrix[row][col])
        if col_val != target:
            return False
        return True