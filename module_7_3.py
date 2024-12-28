import io
from pprint import pprint


class WordsFinder:
    def __init__(self, *files):
        self.file_name = list(files)


    def get_all_words(self):
        all_words = dict()
        symbols = [',', '.', '=', '!', '?', ';', ':', '-']
        for file_name in self.file_name:
            with open(file_name, encoding='utf-8') as file:
                text = file.read().lower()
                for sym in symbols:
                    text = text.replace(sym, '')
                all_words[file_name] = text.split()
        return all_words


    def find(self, word):
        word_find = dict()
        for key, value in self.get_all_words().items():
            for i in range(len(value)):
                if word.lower() == value[i]:
                    word_find[key] = i + 1
                    break
        return word_find

    def count(self, word):
        word_find = dict()
        for key, value in self.get_all_words().items():
            count = 0
            for val in value:
                if word.lower() == val:
                    count += 1
                    word_find[key] = count
        return word_find


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего