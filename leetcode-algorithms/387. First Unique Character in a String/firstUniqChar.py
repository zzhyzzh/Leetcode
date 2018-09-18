class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = {}
        repeatSet = set()
        for i, char in enumerate(s):
            if char not in repeatSet:
                if char not in charMap:
                    charMap[char] = i
                else:
                    charMap.pop(char)
                    repeatSet.add(char)
        return min(charMap.values()) if charMap != {} else -1

solution = Solution()
result = solution.firstUniqChar("leetcode")
print(result)
print(type(result))