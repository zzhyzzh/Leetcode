class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = S.split(" ")
        for i in range(len(S)):
            if S[i][0] in "aeiouAEIOU":
                S[i] += "ma"
            else:
                S[i] = S[i][1:] + S[i][0] + "ma"
            S[i] += "a" * (i + 1)

        return " ".join(S)

solution = Solution()
result = solution.toGoatLatin("I speak Goat Latin")
print(result)
print(type(result))