class Solution(object):
    def letterCheck(self, s, wordDict):
        letterSet = set()
        for word in wordDict:
            for letter in word:
                if letter not in letterSet:
                    letterSet.add(letter)
        for letter in s:
            if letter not in letterSet:
                return False
        return True

    def wordLookUp(self, s, wordDict, dp):
        if len(s) == 0:
            return dp, False
        else:
            if s in wordDict:
                return dp, True
            else:
                for word in wordDict:
                    if s.endswith(word):
                        if s == "":
                            return True
                        else:
                            if len(s) in dp and not dp[len(s)]:
                                return dp, False
                            dp, Status = self.wordLookUp(s[0:len(s) - len(word)], wordDict, dp)
                            if Status:
                                return dp, True
                dp[len(s)] = False
                return dp, False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = sorted(wordDict, key=lambda string: len(string), reverse=True)
        if not self.letterCheck(s, wordDict):
            return False
        dp = {}
        dp, result = self.wordLookUp(s, wordDict, dp)
        return result
