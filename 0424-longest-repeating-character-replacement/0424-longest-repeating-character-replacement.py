class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_freq = 0
        freq_map = {}
        ans = 0
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1
            max_freq = max(max_freq, freq_map[s[end]])
            if end - start + 1 - max_freq > k:
                freq_map[s[start]] = freq_map[s[start]] - 1
                start += 1
            ans = max(ans, end - start + 1 )
        return ans
                
            
        