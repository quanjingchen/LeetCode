class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        find = False
        node = self.root
        def dfs(node, index):
            nonlocal find
            if index == len(word):
                if node.is_end == True:
                    find = True
                return
            for child in node.children:
                if find:
                    return
                if child == word[index] or word[index] == '.':
                    dfs(node.children[child], index + 1)
        dfs(node, 0)
        return find
            
                
            
            
  
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)