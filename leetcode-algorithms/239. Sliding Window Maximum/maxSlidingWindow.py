import collections
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxList = []
        monoQueue = collections.deque()
        for i, num in enumerate(nums):
            # rightmost is the smallest
            while monoQueue and nums[monoQueue[-1]] <= num:
                monoQueue.pop()
            # add in to right
            monoQueue.append(i)
            # leftmost is in-bound
            if i - monoQueue[0] == k:
                monoQueue.popleft()
            # add max
            if i >= k - 1:
                maxList.append(nums[monoQueue[0]])

        return maxList

solution = Solution()
result = solution.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
print(result)
print(type(result))