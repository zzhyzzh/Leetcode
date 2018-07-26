class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        for i in range(len(haystack)):
            if len(haystack) - i < len(needle):
                return -1
            if haystack[i] == needle[0]:
                j = i
                while j - i != len(needle):
                    if haystack[j] != needle[j - i]:
                        break
                    else:
                        j += 1
                if j - i == len(needle):
                    return i
        return -1

solution = Solution()
result = solution.strStr("mississippi", "issipi")
print(result)
print(type(result))