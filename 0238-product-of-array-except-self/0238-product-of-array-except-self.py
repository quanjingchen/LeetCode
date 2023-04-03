class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        prefix = [0] * length
        prefix[0] = 1
        sufix = [0] * length
        sufix[length - 1] = 1
        for i in range(1, length):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            
        for i in reversed(range(len(nums) - 1)):
            sufix[i] = sufix[i + 1] * nums[i + 1]
        
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * sufix[i])
        return ans
            
        