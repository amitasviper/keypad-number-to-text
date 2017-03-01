class Node(object):
    def __init__(self, word):
        self.mapping = {}
        self.terminator = False
        self.create_subnodes(word)
        self.keyboard = {'2': ['A', 'B', 'C'], '3': ['D', 'E', 'F'], '4': ['G', 'H', 'I'],
                         '5': ['J', 'K', 'L'], '6': ['M', 'N', 'O'], '7': ['P', 'Q', 'R', 'S'],
                         '8': ['T', 'U', 'V'], '9': ['W', 'X', 'Y', 'Z']
                         }

    def create_subnodes(self, suffix):
        if suffix == '':
            self.terminator = True
            return
        child_key = suffix[0]
        if self.mapping.has_key(child_key):
            self.mapping[child_key].create_subnodes(suffix[1:])
        else:
            self.mapping[child_key] = Node(suffix[1:])
            self.mapping[child_key]

    def search(self, number, word_in_construction, output_array, root_node, array_in_construction):
        if len(number) == 0:
            if all(len(word) > 3 for word in array_in_construction):
                if len(''.join(array_in_construction)) == 10:
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
                    new_temp_arr = array_in_construction[:]
                self.mapping[letter].search(number[1:], word_in_construction + letter, output_array, root_node,
                                            new_temp_arr)



class RootNode(Node):
    def __init__(self):
        super(RootNode, self).__init__('#')
