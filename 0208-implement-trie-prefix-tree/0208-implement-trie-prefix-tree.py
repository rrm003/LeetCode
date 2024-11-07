class Node:
    def __init__(self):
        self.children = {}
        self.is_last = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        
        curr.is_last = True

    def search(self, word: str) -> bool:
        
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
         
        return curr.is_last 

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            # print(curr.children,"\n", "searching for: " + ch, "flag: ", curr.is_last)
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
            
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)