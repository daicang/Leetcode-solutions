class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while True:
            if i > len(nums)-1:
                return len(nums)
            if nums[i] == val:
                del nums[i]
            else:
                i += 1