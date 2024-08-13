#--------------------------  Создание файла test_file.txt  ---------------------------

__file_name = 'test_file.txt'                            # Присвоение переменной названия файла
file1 = open(__file_name, 'w', encoding='utf-8')         #  Если файла нет, то создается файл products.txt и открывается
file1.write("It's a text for task Найти везде.\nИспользуйте его для cамопроверки.\ntext text text")
file1.close()
class WordsFinder:
    def __init__(self, *file_names):     #  Создаем конструктор WordsFinder где принимаются *file_names
        self.file_names = file_names     #  и сохраняются в self.file_names

    def get_all_words(self):
        all_words = {}                                          # Создаем пустой словарь all_words
        for _file in self.file_names:                           # Для каждого принятого файла (_file - переменная)
            with open(_file, 'r', encoding='utf-8') as file:    # Открываем файл как "file", считываем текст.
                words = [word.strip(',.=!?;: -').lower() for word in file.read().split()]  # Удаляем символы.
                                                                # переводим в нижний регистр,
                                                                # разбиваем на слова по умолчанию пробелом тексте
                all_words[_file] = words               # Сохраняем найденные слова в словарь all_words[_file]
                                                       # где _file - ключ, words - значение

        return all_words                               #  Возвращаем полученный словарь

    def find(self, word):                              # Функция принимающая слова
        all_words = self.get_all_words()               # Получаем созданный функцией self.get_all_words() словарь
        fined_words = {}                               # Создаем пустой словарь fined_words
        for file_name, words in all_words.items():     # Ищем совпадения слов в тексте по индексу
            if word.lower() in words:                  # Если совпадение есть,
                fined_words[file_name] = words.index(word.lower()) + 1  # то записываем в словарь fined_words где
                                                                    #  file_name - ключ,
                                                                    #  words.index(word.lower()) - значение позиции
                                                                    # первого совпадающего слова (+1), т.к. первый - 0
                print(fined_words[file_name], 'result[file_name]')

        return fined_words                             #  Возвращаем полученный словарь

    def count(self, word):                             # Функция принимающая слова
        all_words = self.get_all_words()               # Получаем созданный функцией self.get_all_words() словарь
        word_count = {}                                # Создаем пустой словарь word_count
        for file_name, words in all_words.items():     # Ищем совпадения слов в тексте по индексу
            word_count[file_name] = words.count(word.lower())  # Записываем в словарь word_count где
                                                       #  file_name - ключ,
                                                       #  words.count(word.lower()) - количество совпадений слов
        return word_count                              # Возвращаем полученный словарь


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего