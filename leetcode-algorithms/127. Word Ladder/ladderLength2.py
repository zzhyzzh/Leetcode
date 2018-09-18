class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        wordList.add(endWord)
        wordLen = len(beginWord)
        steps = 1
        BFS = [beginWord]
        while True:
            BFS_next = []
            for reached in BFS:
                for word in wordList:
                    for i in range(wordLen):
                        if reached == word:
                            continue
                        if reached[0:i] == word[0:i] and reached[i + 1:] == word[i + 1:]:
                            if word == endWord:
                                return steps + 1
                            BFS_next.append(word)
            for reached in BFS_next:
                wordList.remove(reached)
            if not BFS_next:
                return 0
            steps += 1
            BFS = BFS_next

solution = Solution()
result = solution.ladderLength(
"hit",
"cog",
["hot","dot","dog","lot","log","cog"]
)
print(result)
print(type(result))

