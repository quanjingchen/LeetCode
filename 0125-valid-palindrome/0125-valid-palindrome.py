class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #step 1: remove all non-alphanumeric characters
        newStr = ''
        for char in s:
            if char.isalnum():
                newStr += char
            
            
        newStr = newStr.lower()
        #step 2: check if it's a palindrome using two pointers
        low = 0
        high = len(newStr) - 1
        while low < high:
            if newStr[low] != newStr[high]:
                return False
            low += 1
            high -= 1
        return True