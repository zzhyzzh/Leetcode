class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        rowLen, colLen = len(matrix), len(matrix[0])
        subRows, subCols = [0, rowLen], [0, colLen]
        SM = []
        while subRows[0] != subRows[1] or subRows[0] != subRows[1]:
            # UP
            line = matrix[subRows[0]][subCols[0]:subCols[1]]
            subRows[0] += 1
            SM += line
            if subRows[0] == subRows[1]:
                return SM
            # RIGHT
            line = []
            for i in range(subRows[0], subRows[1]):
                line.append(matrix[i][subCols[1] - 1])
            subCols[1] -= 1
            SM += line
            if subCols[0] == subCols[1]:
                return SM
            # DOWN
            line = matrix[subRows[1] - 1][subCols[0]:subCols[1]][::-1]
            subRows[1] -= 1
            SM += line
            if subRows[0] == subRows[1]:
                return SM
            #LEFT
            line = []
            for i in range(subRows[0], subRows[1]):
                line.append(matrix[i][subCols[0]])
            subCols[0] += 1
            SM += line[::-1]
            if subCols[0] == subCols[1]:
                return SM



solution = Solution()
result = solution.spiralOrder(
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])
print(result)
print(type(result))