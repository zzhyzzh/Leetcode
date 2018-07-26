class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        PT = []
        rowLen = 1
        for i in range(numRows):
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
        return PT

solution = Solution()
result = solution.generate(5)
print(result)
print(type(result))