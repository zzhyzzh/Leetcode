class Solution:
    def canFinish(self, numCourses, prerequisites):
        n = numCourses
        graph = []
        for i in range(n):
            graph.append([])
        visited = [0] * n
        for a, b in prerequisites:
            graph[a].append(b)

        def DFS(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in graph[i]:
                if not DFS(j):
                    return False
            visited[i] = 1
            return True

        for i in range(numCourses):
            if not DFS(i):
                return False
        return True

