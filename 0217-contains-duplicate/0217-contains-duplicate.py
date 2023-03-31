class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mySet = set()
        for num in nums:
            if num in mySet:
                return True
            else:
                mySet.add(num)
        return False