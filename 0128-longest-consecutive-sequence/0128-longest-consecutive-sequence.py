class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        maxLength = 0
        for num in nums: 
            tmpLen = 1
            if num - 1 not in myset:
                nextNum = num + 1
                while nextNum in myset:
                    tmpLen += 1
                    nextNum += 1
                if tmpLen > maxLength:
                    maxLength = tmpLen
        return maxLength
        