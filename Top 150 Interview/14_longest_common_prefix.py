
from typing import List

class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,word):
        node=self.root
        
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            
            node=node.children[char]

        node.end=True
        
    def longest_common_length(self,word):
        prefix=""
        node=self.root
        
        while node and not node.end and len(node.children)==1:
            char=next(iter(node.children))
            prefix+=char
            node=node.children[char]
            
        return prefix
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        trie_ob=Trie()
        for word in strs:
            trie_ob.insert(word)
            
        return trie_ob.longest_common_length()
    
