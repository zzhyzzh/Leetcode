class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ""
        if numerator * denominator < 0:
            result += "-"
        numerator, denominator = abs(numerator), abs(denominator)
        if numerator > denominator:
            result += str(int(numerator / denominator))
            numerator = numerator % denominator
        else:
            result += "0"
        if numerator == 0:
            return result
        else:
            result += "."
            numerator_list = []
            result_list = []
            curr_numerator = numerator
            while curr_numerator not in numerator_list:
                numerator_list.append(curr_numerator)
                curr_numerator *= 10
                while curr_numerator < denominator:
                    numerator_list.append(curr_numerator)
                    curr_numerator *= 10
                    result_list.append(0)
                result_list.append(int(curr_numerator / denominator))
                curr_numerator = curr_numerator % denominator
                if curr_numerator == 0:
                    for digit in result_list:
                        result += str(digit)
                    return result
            repeat_start = numerator_list.index(curr_numerator)
            for i in range(0, repeat_start):
                result += str(result_list[i])
            result += "("
            for i in range(repeat_start, len(result_list)):
                result += str(result_list[i])
            result += ")"

            return result

solution = Solution()
result = solution.fractionToDecimal(-22, -2)
print(result)
print(type(result))
