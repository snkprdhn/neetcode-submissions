class PrefixTree:

    def __init__(self):
        self.start_dict = {}

    def insert(self, word: str) -> None:
        word_dict = self.start_dict
        for c in word:
            if c in word_dict:
                word_dict = word_dict[c]
            else:
                word_dict[c] = {"is_terminal":False}
                word_dict = word_dict[c]
        
        word_dict["is_terminal"] = True


    def search(self, word: str) -> bool:
        word_dict = self.start_dict
        for c in word:
            if c in word_dict:
                word_dict = word_dict[c]
            else:
                return False
        
        if word_dict["is_terminal"]:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        word_dict = self.start_dict
        for c in prefix:
            if c in word_dict:
                word_dict = word_dict[c]
            else:
                return False
        
        return True
        