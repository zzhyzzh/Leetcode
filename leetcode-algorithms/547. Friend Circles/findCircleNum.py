class DSU(object):
    def __init__(self, M):
        self.N = len(M)
        self.parent = list(range(self.N))
        self.rank = [0] * self.N
        self.count = self.N

    def find(self, pos):
        if self.parent[pos] != pos:
            self.parent[pos] = self.find(self.parent[pos])
        return self.parent[pos]

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

        self.count -= 1
        return True

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        if not M:
            return 0
        dsu = DSU(M)
        for i in range(N):
            for j in range(i, N):
                if M[i][j] == 1:
                    dsu.union(i, j)

        return dsu.count