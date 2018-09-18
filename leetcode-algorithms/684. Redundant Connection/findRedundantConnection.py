class DSU(object):
    def __init__(self):
        self.parent = list(range(1001))
        self.rank = [0] * 1001

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_parent, y_parent = self.find(x), self.find(y)
        if x_parent == y_parent:
            return False
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        else:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        redundant = None
        for edge in edges:
            if not dsu.union(*edge):
                redundant = edge
        return redundant


solution = Solution()
result = solution.findRedundantConnection(
[[1,3],[3,4],[1,5],[3,5],[2,3]]
)
print(result)
print(type(result))