from queue import Queue

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        startPos = 0
        endPos = 0
        for i in range(len(s)):
            if s[i] not in s[startPos:endPos]:
                endPos += 1
                if maxLength < endPos - startPos:
                    maxLength = endPos - startPos
            else:
                repeatPos = s[startPos:endPos].index(s[i])
                if repeatPos == 0:
                    startPos += 1
                    endPos += 1
                else:
                    if maxLength < endPos - startPos:
                        maxLength = endPos - startPos
                    startPos = repeatPos + 1
                    while s[i] == s[startPos] and startPos < endPos:
                        startPos += 1
                    maxLen_remain = self.lengthOfLongestSubstring(s[startPos:])
                    if maxLength < maxLen_remain:
                        maxLength = maxLen_remain
                    break
        return maxLength

solution = Solution()
maxLength = solution.lengthOfLongestSubstring("ohvhjdml");
print(maxLength)



