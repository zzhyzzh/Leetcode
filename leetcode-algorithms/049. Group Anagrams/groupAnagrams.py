class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashTable = {}
        for str in strs:
            key = [0] * 26
            for letter in str:
                key[ord(letter) - 1 - ord("a")] += 1
            key = tuple(key)
            if key not in hashTable:
                hashTable[key] = [str]
            else:
                hashTable[key].append(str)
        anas = []
        for ana in hashTable.values():
            anas.append(ana)

        return anas

solution = Solution()
result = solution.groupAnagrams(
    ["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)
print(type(result))