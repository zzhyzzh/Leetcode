class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1, list2 = [], []
        i = 0
        while i < len(words):
            if words[i] == word1:
                list1.append(i)
            if words[i] == word2:
                list2.append(i)
            i += 1
        pos1, pos2 = 0, 0
        minDist = abs((list1[pos1] - list2[pos2]))
        while pos1 < len(list1) and pos2 < len(list2):
            if list1[pos1] > list2[pos2]:
                minDist = min(list1[pos1] - list2[pos2], minDist)
                pos2 += 1
            elif list1[pos1] < list2[pos2]:
                minDist = min(-list1[pos1] + list2[pos2], minDist)
                pos1 += 1

        return minDist