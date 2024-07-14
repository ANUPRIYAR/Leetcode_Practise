class TrieNode:
    def __init__(self):
        # Initialize children as a dictionary to represent all possible next characters.
        self.children = {}  
        # Flag to check if the current node marks the end of any word.
        self.isEnd = False  
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
        
    def search(self, word: str) -> bool:   
        return self.dfs(word, 0, self.root)

    def dfs(self, word, index, node):
        if index == len(word):
            return node.isEnd

        if word[index] == '.':
            for child in node.children:
                if self.dfs(word, index + 1, node.children[child]):
                    return True
                    
        if word[index] in node.children:
            return self.dfs(word, index + 1, node.children[word[index]])

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)