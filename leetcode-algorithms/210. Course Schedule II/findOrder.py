class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        # a->b
        pointingTo = {}
        pointedBy = {}
        for b, a in prerequisites:
            if a in pointingTo:
                pointingTo[a].append(b)
            else:
                pointingTo[a] = [b]
            if b in pointedBy:
                pointedBy[b].append(a)
            else:
                pointedBy[b] = [a]
        stack = []
        for i in range(n):
            if i not in pointedBy:
                stack.append(i)
        topo = []
        while stack:
            entrance = stack.pop()
            topo.append(entrance)
            if entrance in pointingTo:
                for i in pointingTo[entrance]:
                    pointedBy[i].remove(entrance)
                    if not pointedBy[i]:
                        stack.append(i)
                pointingTo.pop(entrance)

        return topo if not pointingTo else []

solution = Solution()
result = solution.findOrder(
2,
[[1,0]]
)
print(result)
print(type(result))