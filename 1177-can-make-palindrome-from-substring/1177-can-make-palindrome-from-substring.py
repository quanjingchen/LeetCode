class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        #step 1: create a frequency table
        N = 26
        dp = [[0] * N]
        for i in range(1, len(s) + 1):
            new = dp[i - 1][:]
            new[ord(s[i - 1]) - ord('a')] += 1
            dp.append(new)
        #step 2: 
        ans =[]
        for l, h, k in queries:
            oddN = 0
            freq1 = dp[h + 1] 
            freq2 = dp[l]
            freq= [freq1[i] - freq2[i] for i in range(len(freq1))]
            for f in freq:
                if f % 2 != 0:
                    oddN += 1
            if (h - l) % 2 != 0:
                ans.append(oddN <= k * 2)
            else:
                ans.append(oddN - 1 <= k * 2)
        return ans
                
                    
            
            
            
            
