class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dic = {}
        length = 0
        ans = 0
        for i, char in enumerate(s):
            if char in dic:
                left = max(dic[char] + 1, left)
            dic[char] = i
            ans = max(i - left + 1, ans)
        return ans
                
                
            
            
            
        