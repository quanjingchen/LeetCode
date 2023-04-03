class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        prefix.append(1)
        sufix = []
        sufix.append(1)
        for i in range(len(nums)):
            prefix.append(prefix[i] * nums[i])
            
        for i in range(len(nums)):
            sufix.append(sufix[i] * nums[len(nums) - i - 1])
        
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * sufix[len(nums) - i - 1])
        return ans
            
        