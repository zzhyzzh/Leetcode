class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        upwards = True
        former_half = True
        row = 0
        col = 0
        rowSize = len(matrix)
        colSize = len(matrix[0])
        DT = []

        while len(DT) != rowSize * colSize:
            DT.append(matrix[row][col])
            if upwards:
                if col == colSize - 1:
                    row += 1
                    upwards = False
                elif row == 0:
                    col += 1
                    upwards = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == rowSize - 1:
                    col += 1
                    upwards = True
                elif col == 0:
                    row += 1
                    upwards = True
                else:
                    row += 1
                    col -= 1
        return DT


solution = Solution()
result = solution.findDiagonalOrder(
[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(result)
print(type(result))