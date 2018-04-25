from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = defaultdict(int)
        if len(s) != len(t):
            return False
        for letter in s:
            d[letter] += 1
        for letter in t:
            d[letter] -= 1
            if d[letter] < 0:
                return False
        return True

solution = Solution()
result = solution.isAnagram("ab", "a")
print(result)
print(type(result))
