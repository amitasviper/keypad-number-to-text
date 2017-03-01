from trie import Trie
import time
from reverse_index import ReverseIndex


def read_dictionary(filename):
    with open(filename) as f:
        return f.readlines()


def populate_data(data_structure, name):
    print "Constructing %s" % name
    filename = 'dictionary.txt'
    start_time = time.time()
    for line in read_dictionary(filename):
        line = line.strip().upper()
        if len(line) < 3 or len(line) > 10:
            continue
        data_structure.add_word(line)
    print('Construction Time --- %s milli-seconds ---\n' % ((time.time() - start_time) * 1000))


def search(number, data_structure, name):
    start_time = time.time()
    print data_structure.search_words(number)
    print('Searching Time For %s --- %s milli-seconds ---\n' % (name, (time.time() - start_time) * 1000))


if __name__ == '__main__':
    trie = Trie()
    reverse_index = ReverseIndex(3)
    populate_data(trie, '[Trie]')
    populate_data(reverse_index, '[Reverse-Index]')
    while True:
        number = raw_input('Enter number : ')
        search(number, trie, '[Trie]')
        search(number, reverse_index, '[Reverse-Index]')
