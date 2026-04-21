class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add_word(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        res, visit = set(), set()
        n = len(board)
        m = len(board[0])

        def dfs(r,c,node,word):
            if r<0 or c<0 or r==n or c==m or (board[r][c] not in node.children) or (r,c) in visit:
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))

        for i in range(n):
            for j in range(m):
                dfs(i,j,root,"")
        return list(res)