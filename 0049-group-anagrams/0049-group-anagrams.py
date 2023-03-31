class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """            
        ans = collections.defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(str)
        return ans.values()
            

                
                    
                
                
            
            
            