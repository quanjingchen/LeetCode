class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dic = set()
        length = 0
        ans = 0
        for i, char in enumerate(s):
            if char in dic:
                while (s[left] != char):
                    dic.remove(s[left])
                    left += 1
                    length -= 1
                left += 1
                length -= 1
            dic.add(char)
            length += 1
            if length > ans:
                ans = length
        return ans
                
                
            
            
            
        