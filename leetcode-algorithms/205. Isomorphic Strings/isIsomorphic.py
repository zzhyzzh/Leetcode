class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def check(s,t):
            hashMap = {}
            for i in range(len(s)):
                if s[i] not in hashMap:
                    hashMap[s[i]] = t[i]
                else:
                    if hashMap[s[i]] != t[i]:
                        return False
            return True

        return check(s,t) and check(t, s)

solution = Solution()
result = solution.isIsomorphic(s = "egg", t = "add")
print(result)
print(type(result))
