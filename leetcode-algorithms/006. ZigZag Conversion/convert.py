class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) == 1:
            return s
        zigzag = ""
        for i in range(0, min(numRows, len(s))):
            if i == 0 or i == numRows - 1:
                zigzag += s[i::(2*numRows-2)]
            else:
                for j in range(0, len(s), 2*numRows-2):
                    if i < len(s[j:]):
                        zigzag += s[j:][i]
                    if numRows < len(s[j:]) and numRows-2-i < len(s[j:][numRows:]):
                        zigzag += s[j:][numRows:][numRows-2-i]

        return zigzag

solution = Solution()
result = solution.convert("PAYPALISHIRING", 3)
print(result)
print(type(result))
