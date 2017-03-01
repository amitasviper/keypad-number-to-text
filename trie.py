from node import RootNode


class Trie(object):
    def __init__(self):
        self.root = RootNode()

    def add_word(self, word):
        self.root.create_subnodes(word)

    def search(self, number):
        array = []
        self.root.search(number, '', array, self.root, [])
        return array
