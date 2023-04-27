class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        
        def dfs(r, c, node):

            char = board[r][c]
            
            if char not in node.children:
                return
            
            child = node.children[char]
            
            if child.word:
                paths.append(child.word)
                child.word = None
                
            # mark the cell
            board[r][c] = '#'
            # check the neighbors
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, child)
            # clean up
            board[r][c] = char
        
        
        paths = []
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # build the Trie:
        trie = Trie()
        for word in words:
            trie.add(word)
        node = trie.root
        # run the dfs    
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, node)
                
        return paths
            
            
            
        