class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
    
    def lcp(self, word: str, prefixLen: int) -> int:
        node = self.root
        pl = 0
        for ch in word:
            if ch not in node.children:
                return pl
            pl += 1
            node = node.children[ch]
        return min(pl, prefixLen)
            
         

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        mini = 0
        for i in range(1, len(strs)):
            if len(strs[i]) < len(strs[mini]):
                mini = i
        
        trie = Trie()
        trie.insert(strs[mini])
        prefixLen = len(strs[mini])
        for i in range(len(strs)):
            prefixLen = trie.lcp(strs[i], prefixLen)
        return strs[0][:prefixLen]