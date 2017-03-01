from trie import Trie
import time
from rindex import ReverseIndex

def read_dictionary(filename):
    with open(filename) as f:
        return f.readlines()


if __name__ == '__main__':
    trie = Trie()
    reverse_index = ReverseIndex(3)

    filename = 'dictionary.txt'
    start_time = time.time()
    for line in read_dictionary(filename):
        line = line.strip().upper()
        if len(line) < 3 or len(line) > 10:
            continue
        #trie.add_word_to_tree(line)
        reverse_index.add_word(line)

    print('Loading Time --- %s milli-seconds ---' % ((time.time() - start_time) * 1000))


    while True:
        number = raw_input('Enter number : ')
        start_time = time.time()
        #print trie.search(number)
        print reverse_index.search_words(number)
        print("--- %s milli-seconds ---" % ((time.time() - start_time) * 1000))

