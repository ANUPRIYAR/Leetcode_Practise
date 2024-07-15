class Solution:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = [[0]* cols for _ in range(rows)]
        
        trie = Trie()
        trie.insert(word)
        
        node = trie.root
        # print(node.children)
        for i in range(rows):
            for j in range(cols):
                if self.word_found(board, word, i, j, node, visit):
                    return True 

        return False

    def word_found(self, board, word, x, y,  trie, visit):
        char = board[x][y]
        # print(f"char: {char}")
        if char not in trie.children:
            return False

        trie = trie.children[char]
        if trie.eow:
            return True

        visit[x][y] = 1
        for dx, dy in self.directions:
            if (0 <= x + dx < len(board)) and (0 <= y + dy < len(board[0])) and visit[x + dx][y + dy] == 0:
                # print(f"traversing char : {board[x+dx][y+dy]}")
                if self.word_found(board, word, x + dx, y + dy,  trie, visit):
                    # print(f"satisfying char : {board[x+dx][y+dy]}")
                    return True
        visit[x][y] = 0


class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.eow = True 
