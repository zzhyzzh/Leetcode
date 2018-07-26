class Solution(object):
    def ip2int(self, ip):
        ans = 0
        for x in ip.split("."):
            ans = 256*ans + int(x)
        return ans

    def int2ip(self, x):
        return ".".join(str((x >> i) % 256)
            for i in (24, 16, 8, 0))

    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        start = self.ip2int(ip)
        ans = []
        while n:
            mask = max()

solution = Solution()
result = solution.ipToCIDR(ip = "255.0.0.7", n = 10)
print(result)
print(type(result))