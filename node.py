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

    def search(self, number, word_in_construction, output_array, root_node, array_in_construction):
        if len(number) == 0:
            #array.append(output)
            print "Adding array : ", array_in_construction
            output_array.append(array_in_construction)
            return
        digit = number[0]
        for letter in self.keyboard[digit]:
            new_temp_arr = array_in_construction[:]
            if self.mapping.has_key(letter):
                if self.mapping[letter].terminator:
                    new_temp_arr.append(word_in_construction + letter)
                    if self != root_node:
                        root_node.search(number[1:], '', output_array, root_node, new_temp_arr)
                    new_temp_arr = []
                self.mapping[letter].search(number[1:], word_in_construction + letter, output_array, root_node, new_temp_arr)
                new_temp_arr = []

            else:
                #print letter, " is not present, searching from root"
                pass
                #if self != root:
                    #root.search(number[1:], '', array, root)


class RootNode(Node):
    def __init__(self):
        super(RootNode, self).__init__('#')
