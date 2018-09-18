class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        startPos = 0
        endPos = 0
        charT = {}
        charS = {}
        for char in t:
            if char not in charT:
                charT[char] = 1
            else:
                charT[char] += 1
        required = len(charT)
        formed = 0

        minLength = float("inf"), None, None

        while endPos < len(s):
            char = s[endPos]
            charS[char] = charS.get(char, 0) + 1
            if char in charT and charS[char] == charT[char]:
                formed += 1
            while startPos <= endPos and formed == required:
                if endPos - startPos + 1 < minLength[0]:
                    minLength = (endPos - startPos + 1, startPos, endPos)
                char = s[startPos]
                charS[char] -= 1
                if char in charT and charS[char] < charT[char]:
                    formed -= 1
                startPos += 1
            endPos += 1
        return "" if minLength[0] == float("inf") else s[minLength[1]:minLength[2] + 1]


solution = Solution()
result = solution.minWindow("cabwefgewcwaefgcf","cae")
print(result)
print(type(result))