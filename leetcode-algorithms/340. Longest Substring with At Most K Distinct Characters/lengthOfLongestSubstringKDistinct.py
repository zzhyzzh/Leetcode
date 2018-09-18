class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        strIndex = {}
        startPos = 0
        endPos = 0
        maxLength = 0
        if k == 0:
            return 0
        for i, letter in enumerate(s):
            if letter not in strIndex:
                if len(strIndex.keys()) < k:
                    strIndex[letter] = i
                    endPos += 1
                    currLength = endPos - startPos
                    maxLength = max(currLength, maxLength)
                elif len(strIndex.keys()) == k:
                    strIndex[letter] = i
                    lowLetter = s[min(strIndex.values())]
                    startPos = strIndex[lowLetter] + 1
                    strIndex.pop(lowLetter)
                    endPos += 1
                    currLength = endPos - startPos
                    maxLength = max(currLength, maxLength)
            elif letter in strIndex:
                strIndex[letter] = i
                endPos += 1
                currLength = endPos - startPos
                maxLength = max(currLength, maxLength)
        return maxLength

solution = Solution()
result = solution.lengthOfLongestSubstringKDistinct("ababffzzeee", 2)
print(result)
print(type(result))