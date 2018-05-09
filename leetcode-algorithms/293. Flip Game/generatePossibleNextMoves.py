class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        options = []
        notPlus = True
        i = 0
        while i < len(s) - 1:
            if s[i:i + 2] == "++":
                    options.append(s[0:i] + "--" + s[i + 2:])
            i += 1
        return options

solution = Solution()
result = solution.generatePossibleNextMoves("++++")
print(result)
print(type(result))