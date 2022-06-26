class TrieNode:
        # Initialize your data structure here.
        def __init__(self):
            self.word=False
            self.children={}
    
class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    
    def insert(self, word):
        """Inserts word in trie.

        Args:
            word (string): param
            returns None
            
            
        """
        node=self.root
        for i in word:
            if i not in node.children:
                node.children[i]=TrieNode()
            node=node.children[i]
        node.word=True

    
    def search(self, word):
        """
        Args:
            word (string): param

        Returns:
            Boolean: returns if the word is in trie.            
        """
        
        node=self.root
        for i in word:
            if i not in node.children:
                return False
            node=node.children[i]
        return node.word

    
    def startsWith(self, prefix):
        """

        Args:
            prefix (string): param

        Returns:
            boolean: returns if there is any word in trie starts with the given prefix
        """
        node=self.root
        for i in prefix:
            if i not in node.children:
                return False
            node=node.children[i]
        return True
            
    
# Trie  instantiated 
trie = Trie()
print(trie.insert("test")) # insert
print(trie.search("test")) #---> True
print(trie.startsWith("a")) #---> False