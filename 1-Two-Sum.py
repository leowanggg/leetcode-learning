class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return FALSE
        for i in xrange(len(nums)):
            print i
            temp = target - nums[i]
            try:
                j = nums.index(temp)
            except ValueError:
                pass
            else:
                if(i != j):
                    break
        return [i, j]
