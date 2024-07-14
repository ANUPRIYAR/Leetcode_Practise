import math
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        prefix_len = math.inf

        for s in strs:
            trie.insert(s)

        for word in strs:
            prefix_len = min(prefix_len, trie.search(word))

        return strs[0][:prefix_len]

        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow= False

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

    def search(self, word):
        cur = self.root
        prefix_len = 0
        for char in word:
            if len(cur.children) != 1:  # checking if the trie is not branching
                return prefix_len
            cur = cur.children[char]
            prefix_len += 1
        return prefix_len

    def startswith(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False

        return True

