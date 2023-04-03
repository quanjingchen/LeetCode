class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        prefix = [0] * length
        prefix[0] = 1

        for i in range(1, length):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        sufix = 1
        for i in reversed(range(len(nums) - 1)):
            sufix = sufix * nums[i + 1]
            prefix[i] = prefix[i] * sufix
        

        return prefix
            
        