class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = {}
        interList = []
        for num in nums1:
            try:
                inter[num] += 1
            except:
                inter[num] = 1
        for num in nums2:
            if num in inter and inter[num] > 0:
                interList.append(num)
                inter[num] -= 1

        return interList

solution = Solution()
result = solution.intersect(nums1 = [1, 2, 2, 1], nums2 = [2, 2])
print(result)
print(type(result))