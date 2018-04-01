class Solution:
    # def anagramMappings(self, A, B):
    #     """
    #     :type A: List[int]
    #     :type B: List[int]
    #     :rtype: List[int]
    #     """
    #
    #     indices = []
    #     for element in A:
    #         ind = B.index(element)
    #         while ind in indices:
    #             ind = B.index(element, ind + 1)
    #         indices.append(ind)
    #
    #     return indices

    def anagramMappings(self, A, B):
        d = {}
        for i, b in enumerate(B):
            if b not in d:
                d[b] = []
            d[b].append(i)
        return [d[a].pop() for a in A]

solution = Solution()
result = solution.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28])
print(result)
print(type(result))
