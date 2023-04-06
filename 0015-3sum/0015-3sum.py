class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], k: int) -> List[List[int]]:
            seen = set()
            ans = []
            j = 0
            while j < len(nums):
                complement = k - nums[j]
                if complement in seen:
                    ans.append([nums[j], complement])
                    while j + 1 < len(nums) and nums[j + 1] == nums [j]:
                        j += 1
                seen.add(nums[j])
                j += 1  

            return ans
        
        ans = []
        nums.sort()

        for i, num in enumerate(nums):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                res_2sum = twoSum(nums[i+1:], -num)
                for res in res_2sum:
                    ans.append([num, res[0], res[1]])
        return ans

            

                    
                
                
        