class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        currWidth = 0
        lineNum = 1
        for i in range(len(S)):
            currLetter = widths[ord(S[i]) - ord("a")]
            if currWidth + currLetter <= 100:
                currWidth += currLetter
            else:
                lineNum += 1
                currWidth = currLetter

        return [lineNum, currWidth]



solution = Solution()
result = solution.numberOfLines(
    [10,10,10,10,10,10,10,10,10,
     10,10,10,10,10,10,10,10,10,
     10,10,10,10,10,10,10,10],
    "abcdefghijklmnopqrstuvwxyz")
print(result)
print(type(result))