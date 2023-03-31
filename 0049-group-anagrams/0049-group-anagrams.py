class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """            
        ans = {}
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in ans:
                ans[tuple(count)].append(str)
            else:
                ans[tuple(count)] = [str]
        return ans.values()
            

                
                    
                
                
            
            
            