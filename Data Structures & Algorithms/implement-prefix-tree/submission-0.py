class TrieNode:
    def __init__(self):
        self.children={} #hash map where current char is the key
        self.end=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for char in word:
            if char not in cur.children:
                #make a new node!
                cur.children[char] = TrieNode()
            cur=cur.children[char]
        cur.end=True #set last node to be the end of the word


    def search(self, word: str) -> bool:
        cur=self.root
        for char in word:
            if char not in cur.children:
                return False
            cur=cur.children[char]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        #same as search except we don't care if its the end of the word
        cur=self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur=cur.children[char]
        return True
        