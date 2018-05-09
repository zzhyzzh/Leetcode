class Solution(object):
    dict = {}
    def __init__(self):
        for letter in "qwertyuiop":
            self.dict[letter] = 1
        for letter in "asdfghjkl":
            self.dict[letter] = 2
        for letter in "zxcvbnm":
            self.dict[letter] = 3

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output = []
        for word in words:
            word_ = word.lower()
            row = self.dict[word_[0]]
            for i in range(1, len(word_)):
                if self.dict[word_[i]] != row:
                    break
            else:
                output.append(word)

        return output

solution = Solution()
result = solution.findWords(["Hello", "Alaska", "Dad", "Peace"])
print(result)
print(type(result))
