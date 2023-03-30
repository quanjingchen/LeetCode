class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == ')' and (len(stack) == 0 or stack.pop() != '('):
                return False
            if i == '}' and (len(stack) == 0 or stack.pop() != '{'):
                return False
            if i == ']' and (len(stack) == 0 or stack.pop() != '['):
                return False
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
                
        return len(stack) == 0
            
            