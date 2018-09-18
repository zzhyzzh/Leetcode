import math
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix == []:
            return
        n = len(matrix)
        for i in range(n/2):
            for j in range(n - n/2):
                temp = matrix[i][j]
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]

solution = Solution()
result = solution.rotate([[1,2,3],[4,5,6],[7,8,9]])
print(result)
print(type(result))