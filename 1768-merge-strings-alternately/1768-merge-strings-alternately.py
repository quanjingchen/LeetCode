class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        len_1 = len(word1)  
        len_2 = len(word2)
        i = 0;
        while i < max(len_1, len_2): 
            if i < len_1:
                ans += word1[i]
            if i < len_2:
                ans += word2[i]
            i+=1
        return ans
                
            
        
            
            
        