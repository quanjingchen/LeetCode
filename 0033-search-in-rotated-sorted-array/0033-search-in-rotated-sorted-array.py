class Solution(object):
    @staticmethod
    def find_min(nums):
        low = 0
        high = len(nums) - 1
        if nums[low] < nums[high]:
            return low
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1 
        return low
    
    @staticmethod
    def binarySearch(nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1 
            else:
                return mid
        return -1
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_index = Solution.find_min(nums)

        if min_index == 0:
            return Solution.binarySearch(nums, target)
        if target >= nums[0]:
            return Solution.binarySearch(nums[:min_index], target)
        ans = Solution.binarySearch(nums[min_index:], target)
        if ans == -1:
            return -1
        return ans + min_index
