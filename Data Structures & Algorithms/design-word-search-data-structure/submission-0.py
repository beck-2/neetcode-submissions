class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
class WordDictionary:
    #REIMPLEMENT BUT PAY ATTENTION TO DOTS... a dot should mean you explore all children for all nodes.. recursively?
    #use a trie lol
    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children: #don't need to worry abput * because those are only in search
                #newnode
                cur.children[c] = TrieNode()
            cur=cur.children[c]
        cur.isEnd=True
        
        

    def search(self, word: str) -> bool:
        def dfs(j: int, node):
            cur=node
            for i in range(j, len(word)):
                c=word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1,child): return True
                    return False
                if c not in cur.children:
                    return False
                cur=cur.children[c]
            return cur.isEnd
        return dfs(0,self.root)




"""
        #we don't need a is prefix
        cur=self.root
        for i, c in enumerate(word):
            if c==".":
                for child in cur.children: #explore all possible paths
                    if self.search(child, word[(i+1):]): return True
                return False
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.isEnd
    """
    
