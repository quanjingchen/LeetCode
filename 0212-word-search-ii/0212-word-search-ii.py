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
            if child.word is not None:
                paths.append(child.word)
                child.word = None  # Remove the word to prevent duplicates
            
            #remove the leaf node
            if len(child.children) == 0:
                node.children.pop(char)
                return

            board[r][c] = '#'  # Mark the cell as visited
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, child)
            board[r][c] = char  # Restore the cell
            

                

        paths = []
        rows, cols = len(board), len(board[0])

        trie = Trie()
        for word in words:
            trie.add(word)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)

        return paths