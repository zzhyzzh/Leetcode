class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == "C":
                    stack.pop()
            elif op == "D":
                    stack.append(stack[-1] * 2)
            elif op == "+":
                    stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)

solution = Solution()
result = solution.calPoints(["5","-2","4","C","D","9","+","+"])
print(result)
print(type(result))