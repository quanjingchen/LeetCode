class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic={}
        
        
        for index, i in enumerate(nums):
            if i in dic:
                dic[i].append(index)
            else:
                dic[i]=[index]
                
        
        
        for index, i in enumerate(nums):
            b = target - i
            if b == i and b in dic and len(dic[i]) > 1:
                return [dic[i][0], dic[i][1]]
            elif b!= i and b in dic:
                return [dic[i][0], dic[b][0]]
                
                
            