class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        if (ord(coordinates[0]) - ord('a') + 1) % 2 == int(coordinates[1]) % 2:
            return False
        else:
            return True
        