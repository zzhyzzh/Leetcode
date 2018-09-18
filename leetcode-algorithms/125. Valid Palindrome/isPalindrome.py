class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            while not s[i].isalpha() and not s[i].isdigit():
                i += 1
                if i > len(s) - 1:
                    return True
            while not s[j].isalpha() and not s[j].isdigit():
                j -= 1
                if j < 0:
                    return True
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


