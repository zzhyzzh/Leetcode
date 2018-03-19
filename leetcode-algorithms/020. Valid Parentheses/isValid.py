class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        if len(s) < 2:
            return False
        for token in s:
            if token in ["(", "[", "{"]:
                stack.append(token)
            elif token in [")", "]", "}"]:
                if stack == []:
                    return False
                elif token == ")" and stack[len(stack) - 1] == "(":
                        stack.pop()
                elif token == "]" and stack[len(stack) - 1] == "[":
                        stack.pop()
                elif token == "}" and stack[len(stack) - 1] == "{":
                        stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False

solution = Solution()
result = solution.isValid("[])")
print(result)
print(type(result))