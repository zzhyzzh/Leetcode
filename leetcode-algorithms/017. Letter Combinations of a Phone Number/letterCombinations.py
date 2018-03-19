class Solution:
    def int_to_char(self, intStr):
        switcher = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        return switcher.get(intStr)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        combi_list = []
        if digits == "":
            return []
        char_list = self.int_to_char(digits[0])
        if len(digits) == 1:
            return char_list
        else:
            rest_combi = self.letterCombinations(digits[1:])
            for char in char_list:
                for combi in rest_combi:
                    combi_list.append(char + combi)

        return combi_list

solution = Solution()
result = solution.letterCombinations("234")
print(result)
print(type(result))