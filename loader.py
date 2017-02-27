from tree import Tree


def read_dictionary(filename):
    with open(filename) as f:
        return f.readlines()


if __name__ == "__main__":
    tree = Tree()
    tree.add_word_to_tree("AMIT")
    tree.add_word_to_tree("AMITKUMAR")
    tree.add_word_to_tree("BAMITKUMAR")
    print tree.search("AMITA", 23456789)
