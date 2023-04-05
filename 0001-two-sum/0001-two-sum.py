class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        ans = []
        for i, num in enumerate(nums):
            if num not in freq:
                freq[num] = []
            freq[num].append(i)
                
        for i, num in enumerate(nums):
            if target - num in freq:
                for j in freq[target - num]:
                    if j != i:
                        ans.append([i, j])
        return ans[0]        