class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        formed = 0
        freq_window = {}
        freq_t = Counter(t)
        counts_unique = len(freq_t)
        ans = float('inf'), None, None
        for r,char in enumerate(s):
            if char in freq_t:
                freq_window[char] = freq_window.get(char, 0) + 1
                if freq_window[char] == freq_t[char]:
                    formed += 1
                
                while r >= l and formed == counts_unique:
                    if r - l + 1 < ans[0]:
                        ans = r - l + 1, l , r
                    if s[l] in freq_t:
                        if freq_window[s[l]] == freq_t[s[l]]:
                            formed -= 1                        
                        freq_window[s[l]] -= 1

                    l += 1
                
        return '' if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]