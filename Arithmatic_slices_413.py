class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slice_list = []
        for slices in nums:
            if len(nums) < 1:
                return 0
            slice_list.append(slices)
            slice(slice_list[1 : len(nums) : 0])
