class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # assure len(nums1) > len(nums2)
        if len(nums1) < len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        # search based on shorter list
        cut_2 = len(nums2)
        while True:
            cut_1 = (len(nums1) + len(nums2) - cut_2)

            LeftBound_2 = -float('inf') if cut_2 == 0 else nums2[int((cut_2-1)/2)]
            RightBound_2 = float('inf') if int(cut_2/2) == len(nums2) else nums2[int(cut_2/2)]

            LeftBound_1 = -float('inf') if cut_1 == 0 else nums1[int((cut_1-1)/2)]
            RightBound_1 = float('inf') if int(cut_1/2) == len(nums1) else nums1[int(cut_1 / 2)]

            if LeftBound_1 > RightBound_2:
                cut_2 += 1
            elif LeftBound_2 > RightBound_1:
                cut_2 -= 1
            elif LeftBound_1 <= RightBound_2 and LeftBound_2 <= RightBound_1:
                return (max(LeftBound_1, LeftBound_2) + min(RightBound_1, RightBound_2))/2

nums1 = [1, 2]
nums2 = [3, 4]
solution = Solution()
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)
print(type(result))