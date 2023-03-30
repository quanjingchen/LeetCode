class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {')': '(', ']': '[', '}': '{'};
        
        for char in s:
            if char in dic:
                topElement = stack.pop() if stack else '^'
                if topElement != dic[char]:
                    return False
            else:
                stack.append(char)
             
        return not stack
            
            