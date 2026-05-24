class PrefixTree:
    class Node:
        def __init__(self, char=""):
            self.letter = char
            self.nextLetter = dict()
            self.endOfWord = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.nextLetter:
                node = node.nextLetter[char]
            else:
                node.nextLetter[char] = self.Node(char)
                node = node.nextLetter[char]
        node.endOfWord = True


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.nextLetter:
                return False
            node = node.nextLetter[char]
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.nextLetter:
                return False
            node = node.nextLetter[char]
        return True
        
        
        