class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        stack = []
        num = 0
        sign = "+"
        for i, token in enumerate(s):
            if token.isdigit():
                num = num * 10 + int(token)
            if not token.isdigit() or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                # truncate toward zero
                # consider when num is negative
                elif sign == "/":
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = token
                num = 0

        return sum(stack)

