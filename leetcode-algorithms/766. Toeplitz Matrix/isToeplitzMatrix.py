class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        diagonal = [False] * (max(row, col) + min(row, col) - 1)
        for i in range(row):
            for j in range(col):
                if diagonal[i - j] is False:
                    diagonal[i - j] = matrix[i][j]
                elif diagonal[i - j] != matrix[i][j]:
                    return False

        return True

solution = Solution()
result = solution.isToeplitzMatrix([[58,25,63],[30,58,25],[90,30,58]])
print(result)
print(type(result))