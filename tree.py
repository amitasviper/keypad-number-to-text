from node import RootNode


class Tree(object):
    def __init__(self):
        self.root = RootNode()
        self.keyboard = {}

    def add_word_to_tree(self, word):
        self.root.create_subnodes(word)

    def search(self, word, number):
        return self.root.search(word)

