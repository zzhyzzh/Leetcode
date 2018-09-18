class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        PT = []
        rowLen = 1
        for i in range(rowIndex + 1):
            row = []
            for j in range(rowLen):
                if j == 0 or j == rowLen - 1:
                    row.append(1)
                else:
                    row.append(
                        PT[len(PT) - 1][j - 1] +
                        PT[len(PT) - 1][j]
                    )
            rowLen += 1
            PT.append(row)
        return PT[-1]

solution = Solution()
result = solution.getRow(3)
print(result)
print(type(result))