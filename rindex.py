from itertools import combinations, product


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

    def get_word_index(self, word):
        number = 0
        for letter in word:
            number = (number*10) + self.mapping(letter)
        return str(number)

    def add_word(self, word):
        index = self.get_word_index(word)
        if self.indexedData.has_key(index):
            self.indexedData[index].append(word)
        else:
            self.indexedData[index] = [word]

    def combine_lists(self, prefix_list, suffix_list):
        combined = []
        for prefix in prefix_list:
            for suffix in suffix_list:
                combined.append([prefix, suffix])
        return combined

    def split_combinations(self, number):
        for split in range(1, len(number)):
            for combination in self.split_combinations(number[split:]):
                yield [number[:split]] + combination
        yield [number]

    def split_combinations2(self, number):
        for i in range(len(s)):
            for split_points in combinations(range(1, len(number)), i):
                yield self.split_string(number, split_points)

    def split_string(self, number, index):
        return [number[start:finish] for start, finish in zip((None,) + index, index + (None,))]

    def words_for_number(self, number_array):
        result = []
        for number in number_array:
            result.append(self.indexedData[number])
        result = [list(tup) for tup in product(*result)]
        return result

    def search_words(self, number):
        result = []
        splitted_number_cominations = self.split_combinations(number)
        for splitted_number in splitted_number_cominations:
            if len(splitted_number) > 2:
                continue
            if all(len(number) >= self.min_word_len and self.indexedData.has_key(number) for number in splitted_number):
                splitted_word = self.words_for_number(splitted_number)
                result.extend(splitted_word)
        return result

