from tree import Tree
import time

def read_dictionary(filename):
    with open(filename) as f:
        return f.readlines()


if __name__ == "__main__":
    tree = Tree()
    filename = 'dictionary.txt'
    #filename = 'temp.txt'
    number = '6686787825'  # 6787825'
    start_time = time.time()
    for line in read_dictionary(filename):
        line = line.strip().upper()
        tree.add_word_to_tree(line)

    print("Loading Time --- %s milli-seconds ---" % ((time.time() - start_time) * 1000))

    while True:
        print "Number is ", number,
        raw_input()
        start_time = time.time()
        print tree.search(number)
        print("--- %s milli-seconds ---" % ((time.time() - start_time) * 1000))

