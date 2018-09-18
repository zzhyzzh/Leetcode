class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hastTable = {}
        for str in strings:
            pattern = []
            for i in range(1, len(str)):
                dif = ord(str[i]) - ord(str[0])
                if dif < 0:
                    dif = 26 + dif
                pattern.append(dif)
            pattern = tuple(pattern)
            if pattern not in hastTable:
                hastTable[pattern] = [str]
            else:
                hastTable[pattern].append(str)
        groupStr = []
        for group in hastTable.values():
            groupStr.append(group)

        return groupStr


solution = Solution()
result = solution.groupStrings(
    ["ab", "ba"])
print(result)
print(type(result))