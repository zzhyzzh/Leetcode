class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [0] * (rowIndex + 1)
        row[0] = 1
        for i in range(rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]

        return row

solution = Solution()
result = solution.getRow(3)
print(result)
print(type(result))