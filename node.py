class Node(object):
    def __init__(self, word):
        self.mapping = {}
        self.word = word
        self.terminator = False
        self.create_subnodes(word)
        self.keyboard = {'2': ['A', 'B', 'C'], '3': ['D', 'E', 'F'], '4': ['G', 'H', 'I'],
                         '5': ['J', 'K', 'L'], '6': ['M', 'N', 'O'], '7': ['P', 'Q', 'R', 'S'],
                         '8': ['T', 'U', 'V'], '9': ['W', 'X', 'Y', 'Z']
                         }

    def create_subnodes(self, suffix):
        #print "Adding : ",suffix
        if suffix == '':
            self.terminator = True
            return
        child_key = suffix[0]
        if self.mapping.has_key(child_key):
            self.mapping[child_key].create_subnodes(suffix[1:])
        else:
            # if suffix[1:] == '':
            #     self.terminator = True
            #     return
            self.mapping[child_key] = Node(suffix[1:])

    def search(self, number, output, array):
        if len(number) == 0:
            array.append(output)
            return
        digit = number[0]
        for letter in self.keyboard[digit]:
            print 'Looking for : ',letter
            print "Keys: ", self.mapping.keys()
            if self.mapping.has_key(letter):
                print "Letter is present : ", letter
                self.mapping[letter].search(number[1:], output + letter, array)
            else:
                print letter, " is not present"

class RootNode(Node):
    def __init__(self):
        super(RootNode, self).__init__('#')
