from itertools import product


class ReverseIndex(object):
    def __init__(self, min_word_len):
        self.indexedData = {}
        self.min_word_len = min_word_len

    def mapping(self, letter):
        if letter in 'abcABC': return 2
        if letter in 'defDEF': return 3
        if letter in 'ghiGHI': return 4
        if letter in 'jklJKL': return 5
        if letter in 'mnoMNO': return 6
        if letter in 'pqrsPQRS': return 7
        if letter in 'tuvTUV': return 8
        if letter in 'wxyzWXYZ': return 9

    def calculate_word_index(self, word):
        number = 0
        for letter in word:
            number = (number * 10) + self.mapping(letter)
        return str(number)

    def add_word(self, word):
        index = self.calculate_word_index(word)
        if self.indexedData.has_key(index):
            self.indexedData[index].append(word)
        else:
            self.indexedData[index] = [word]

    def split_number_combinations(self, number):
        splitted_numbers = [[number]]
        for i in range(0, 10 - 2 * self.min_word_len):
            split_index = self.min_word_len + i
            prefix = number[:split_index]
            suffix = number[split_index:]
            splitted_numbers.append([prefix, suffix])
        return splitted_numbers

    def words_for_number(self, number_array):
        result = []
        for number in number_array:
            result.append(self.indexedData[number])
        result = [list(tup) for tup in product(*result)]
        return result

    def search_words(self, number):
        result = []
        splitted_numbers = self.split_number_combinations(number)
        for splitted_number in splitted_numbers:
            if all(len(number) >= self.min_word_len and self.indexedData.has_key(number) for number in splitted_number):
                splitted_word = self.words_for_number(splitted_number)
                result.extend(splitted_word)
        return result
