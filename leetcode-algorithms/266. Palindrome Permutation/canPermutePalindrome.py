class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        wordDic = {}
        for letter in s:
            if wordDic.get(letter, 0):
                wordDic[letter] += 1
            else:
                wordDic[letter] = 1
        oddExist = False
        for letter in wordDic:
            if wordDic[letter] % 2 == 0:
                continue
            else:
                if not oddExist:
                    oddExist = True
                else:
                    return False
        return True


solution = Solution()
result = solution.canPermutePalindrome("carerac")
print(result)
print(type(result))