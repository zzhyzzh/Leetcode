class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        startPos = 0
        endPos = 0
        indexTable = {}
        while endPos < len(s) and startPos <= endPos:
            if s[endPos] not in indexTable or indexTable[s[endPos]] < startPos:
                indexTable[s[endPos]] = endPos
                maxLength = max(maxLength, endPos - startPos + 1)
            else:
                startPos = indexTable[s[endPos]] + 1
                maxLength = max(maxLength, endPos - startPos + 1)
                indexTable[s[endPos]] = endPos
            endPos += 1
        return maxLength

solution = Solution()
maxLength = solution.lengthOfLongestSubstring("abcabcbb")
print(maxLength)



