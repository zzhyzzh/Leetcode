class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pos = -1
        pos_list = []
        output = [-1] * len(S)
        while True:
            C_pos = S.find(C, pos + 1)
            if C_pos == -1:
                break
            pos_list.append(C_pos)
            output[C_pos] = 0
            pos = C_pos
        for pos in pos_list:
            distance = 1
            for i in range(pos - 1, -1, -1):
                if output[i] < 0 or output[i] > distance:
                    output[i] = distance
                    distance += 1
                else:
                    break
            distance = 1
            for i in range(pos + 1, len(S)):
                if output[i] < 0:
                    output[i] = distance
                    distance += 1
                else:
                    break

        return output


solution = Solution()
result = solution.shortestToChar("baaa", "b")
print(result)
print(type(result))