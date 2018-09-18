class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        said = "1"
        for i in range(1, n):
            newSay = ""
            stack = []
            for digit in said:
                if stack and stack[-1] == digit:
                    stack.append(digit)
                elif stack and stack[-1] != digit:
                    newSay += str(len(stack)) + stack[0]
                    stack = [digit]
                else:
                    stack.append(digit)
            if stack:
                newSay += str(len(stack)) + stack[0]
            said = newSay

        return said


solution = Solution()
result = solution.countAndSay(
4
)
print(result)
print(type(result))