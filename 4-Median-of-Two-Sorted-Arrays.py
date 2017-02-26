class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newNums = nums1 + nums2
        newNums.sort()
        N = len(newNums)
        if N % 2 == 0:
            median = (newNums[N/2] + newNums[N/2-1])/2.0
        else:
            median = newNums[N/2]
        return median
