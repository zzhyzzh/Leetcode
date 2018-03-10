class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxVol = min(height[right], height[left]) * (right - left)
        while left < right:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            maxVol = max(maxVol, min(height[right], height[left]) * (right - left))

        return maxVol
solution = Solution()
result = solution.maxArea([1,1]);
print(result)



