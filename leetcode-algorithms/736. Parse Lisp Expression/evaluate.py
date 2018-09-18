class Solution(object):

    def isNumber(self, expression):
        if expression[0] in "-0123456789":
            return True
        else:
            return False

    def isVar(self, expression):
        if expression[0] in "abcdefghijklmnopqrstuvwxyz":
            return True
        else:
            return False

    def isExpression(self, expression):
        if expression[0] == "(":
            return True
        else:
            return False

    def numberValue(self, expression):
        value = 1
        if expression[0] == "-":
            expression = expression[1:]
            value = -1
        if expression.find(" ") == -1:
            value = value * int(expression)
            return value, ""
        else:
            i = expression.find(" ") - 1
            value = value * int(expression[:i + 1])
            return value, expression[i + 2:]

    def varFind(self, expression):
        if expression.find(" ") == -1:
            return expression, ""
        else:
            i = expression.find(" ") - 1
            return expression[:i + 1], expression[i + 2:]

    def elementFind(self, expression, varTable):
        if self.isNumber(expression):
            element, expression = self.numberValue(expression)
        elif self.isVar(expression):
            var, expression = self.varFind(expression)
            if var in varTable:
                element = varTable[var]
        elif self.isExpression(expression):
            element, expression = self.parseLisp(expression, varTable)
        return element, expression

    def parseLisp(self, expression, varTable):
        varTable_scope = varTable.copy()
        stack = []
        for i in range(len(expression)):
            if expression[i] == "(":
                stack.append("(")
            elif expression[i] == ")":
                stack.pop()
            if stack == []:
                if i == len(expression) - 1:
                    remain = ""
                else:
                    remain = expression[i + 2:]
                    expression = expression[:i + 1]
                break
        expression = expression[1:len(expression) - 1]
        if expression.startswith("add"):
            add1, add2 = 0, 0
            expression = expression[4:]
            add1, expression = self.elementFind(expression, varTable_scope)
            add2, expression = self.elementFind(expression, varTable_scope)
            return add1 + add2, remain
        elif expression.startswith("mult"):
            expression = expression[5:]
            mult1, mult2 = 0, 0
            mult1, expression = self.elementFind(expression, varTable_scope)
            mult2, expression = self.elementFind(expression, varTable_scope)
            return mult1 * mult2, remain
        elif expression.startswith("let"):
            expression = expression[4:]
            while True:
                temp_expression = expression
                temp_varTable = varTable_scope.copy()
                try:
                    if self.isVar(expression):
                        var, expression = self.varFind(expression)
                        value, expression = self.elementFind(expression, varTable_scope)
                        varTable_scope[var] = value
                    else:
                        value, expression = self.elementFind(expression, varTable_scope)
                        break
                except:
                    value, expression = self.elementFind(temp_expression, temp_varTable)
                    break
            return value, remain

    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        value, _ = self.parseLisp(expression, {})
        return value


solution = Solution()
result = solution.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))")
print(result)
print(type(result))