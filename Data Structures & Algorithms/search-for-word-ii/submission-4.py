class Node:
    def __init__(self):
        self.cldrn = {}
        self.eow = False
        self.word = ""
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.cldrn:
                node.cldrn[ch] = Node()
            node = node.cldrn[ch]
        node.eow = True
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tr = Trie()
        for word in words:
            tr.insert(word)
        root = tr.root

        m = len(board)
        n = len(board[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        res = []

        def find_word(i, j, node):
            nonlocal res

            if board[i][j] == "#":
                return False
            
            ch = board[i][j]
            board[i][j] = "#"

            if node.eow:
                res.append(node.word)
                node.eow = False
            
            for r, c in dirs:
                new_r = i+r
                new_c = j+c
                if (0 <= new_r < m) and (0 <= new_c < n):
                    new_ch = board[new_r][new_c]
                    if new_ch != "#" and new_ch in node.cldrn:
                        if find_word(new_r, new_c, node.cldrn[new_ch]):
                            node.cldrn.pop(new_ch)

            board[i][j] = ch

            if not node.cldrn and not node.eow:
                return True

            return False

        
        for r in range(m):
            for c in range(n):
                if board[r][c] in root.cldrn:
                    find_word(r, c, root.cldrn[board[r][c]])
        
        return res