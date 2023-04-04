class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('/')
            res.append(s)
        return ''.join(res)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res, i = [], 0
        while i < len(s):
            idx = s[i:].find('/')
            size = int(s[i:i+idx])
            res.append(s[i+idx+1:i+idx+size+1])
            i += idx+size+1
        return res