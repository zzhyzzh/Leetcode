class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        (+-) (number) . number e (+-) number
        '''
        s = s.strip(" ")
        if s == "":
            return False

        def isSign(s):
            if s[0] in "+-":
                return True
            else:
                return False

        def isSingleNumber(s, withSign):
            i = 0
            NumberExist = False
            if withSign and isSign(s):
                i += 1
            while i < len(s):
                if s[i] not in "0123456789":
                    break
                i += 1
                NumberExist = True
            return i, NumberExist

        def isDecimal(s):
            i = 0
            add = 0
            NumberExist_post = False
            i, NumberExist_pre = isSingleNumber(s[i:], True)
            if i < len(s) and s[i] == ".":
                i += 1
                if i < len(s):
                    add, NumberExist_post = isSingleNumber(s[i:], False)
            if not NumberExist_post and not NumberExist_pre:
                return 0
            else:
                return i + add

        i = 0
        i += isDecimal(s)
        if i > 0 and i + 1 < len(s) and s[i] == "e":
            add, exist = isSingleNumber(s[i + 1:], True)
            if exist:
                i = i + add + 1
        if i == len(s):
            return True
        else:
            return False

solution = Solution()
result = solution.isNumber("2e+1")
print(result)
print(type(result))