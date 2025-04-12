

class TrieNode:
    def __init__(self):
        self.children={}
        self.exists=False


class WordDictionary:


    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        node=self.root

        for char in word:
            if not char in node.children:
                node.children[char]=TrieNode()

            node=node.children[char]

        node.exists=True

    def search(self, word: str) -> bool:

        def dfs(index,word,node):
            if index==len(word):
                # print(node.exists)
                return node.exists

            char=word[index]
            if char==".":
                for c in node.children:
                    if dfs(index+1,word,node.children[c]):
                        return True
                
                return False
            elif char in node.children:
                return dfs(index+1,word,node.children[char])
            else:
                return False
        
        return dfs(0,word,self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)