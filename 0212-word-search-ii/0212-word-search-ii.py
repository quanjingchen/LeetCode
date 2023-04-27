class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ''

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
            if node.word:
                paths.add(node.word)
            if not node.children:
                return
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            if board[r][c] not in node.children:
                return
            
            char = board[r][c]
            board[r][c] = '#'
            for neighbor in neighbors:
                new_r = r + neighbor[0]
                new_c = c + neighbor[1]
                dfs(new_r, new_c, node.children[char])
            board[r][c] = char

        paths = set()
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        trie = Trie()
        for word in words:
            trie.add(word)
        node = trie.root

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, node)

        return list(paths)