class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_eow = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                c = word[i]
                if c != ".":
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                else:
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
            return cur.is_eow
        
        return dfs(0, self.root)