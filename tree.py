from node import RootNode


class Tree(object):
    def __init__(self):
        self.root = RootNode()
        self.keyboard = {'2': ['A', 'B', 'C'], '3': ['D', 'E', 'F'], '4': ['G', 'H', 'I'],
                         '5': ['J', 'K', 'L'], '6': ['M', 'N', 'O'], '7': ['P', 'Q', 'R', 'S'],
                         '8': ['T', 'U', 'V'], '9': ['W', 'X', 'Y', 'Z']
                         }

    def add_word_to_tree(self, word):
        self.root.create_subnodes(word)

    def search(self, number):
        array = []
        self.root.search(number, '', array, self.root, [])
        print array

