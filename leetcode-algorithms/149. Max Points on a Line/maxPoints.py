class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)

        d = defaultdict(int)
        result = 0
        for i in range(len(points)):
            d.clear()
            overlap, currentMax = 0, 0
            for j in range(i + 1, len(points)):
                dx = points[i].x - points[j].x
                dy = points[i].y - points[j].y
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                gcd = self.getGcd(dx, dy)
                dx //= gcd
                dy //= gcd
                d[(dx, dy)] += 1
                currentMax = max(currentMax, d[(dx, dy)])
            result = max(result, currentMax + overlap + 1)
        return result

    def getGcd(self, a, b):
        if b == 0:
            return a
        return self.getGcd(b, a%b)