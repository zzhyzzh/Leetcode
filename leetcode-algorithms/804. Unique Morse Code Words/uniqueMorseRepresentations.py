class Solution:
    def letter_to_morse(self, letter):
        morse = [".-", "-...", "-.-.",
             "-..", ".", "..-.",
             "--.", "....", "..",
             ".---", "-.-", ".-..",
             "--", "-.", "---",
             ".--.", "--.-", ".-.",
             "...", "-", "..-",
             "...-", ".--", "-..-",
             "-.--", "--.."]
        return morse[ord(letter) - ord("a")]

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        unique = set()
        for word in words:
            morse = ""
            for letter in word:
                morse += self.letter_to_morse(letter)
            unique.add(morse)

        return len(unique)

solution = Solution()
result = solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
print(result)
print(type(result))
