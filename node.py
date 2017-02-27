class Node(object):
    def __init__(self, word):
        self.mapping = {}
        self.word = word
        self.letter = word[0]
        self.create_subnodes(word[1:])

    def create_subnodes(self, suffix):
        if suffix == '':
            return
        child_key = suffix[0]
        if self.mapping.has_key(child_key):
            print "Inserting in Already present Node", suffix
            self.mapping[child_key].create_subnodes(suffix[1:])
        else:
            print "Creating a NEW Node", suffix
            self.mapping[child_key] = Node(suffix)

    def search(self, word):
        if len(word) == 0:
            print "Returning true from  1"
            return True
        letter = word[0]
        if not self.mapping.has_key(letter):
            print "Returning false from  2"
            return False
        return self.mapping[letter].search(word[1:])

class RootNode(Node):
    def __init__(self):
        super(RootNode, self).__init__('#')
