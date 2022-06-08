from pathlib import Path
from typing import Dict, Any, List, Optional
import csv

def count_words(text: str) -> Dict[str, int]:
    """
    Функция для подсчета слов в тексте.

    При подсчете слов - все знаки препинания игнорируются.
    Словом считается непрерывная последовательность длиной больше одного
    символа, состоящая из букв в диапазоне A-Z и a-z.
    Если в последовательности присутствует цифра - это не слово.

    Hello - слово
    Hello7 - не слово

    При подсчете слов регистр букв не имеет значения.

    Результат выполнения функции словарь, в котором:
    ключ - слово в нижнем регистре
    значение - количество вхождений слов в текст

    :param text: текст, для подсчета символов
    :return: словарь, в котором:
             ключ - слово в нижнем регистре
             значение - количество вхождений слов в текст
    """

    punctuation_marks = {'.', ',', ':', '?', '!'}
    answer = {}
    words = text.split(' ')
    while ' ' in words:
        words.remove(' ')

    while '' in words:
        words.remove('')

    for i, word in enumerate(words):
        while words[i][-1] in punctuation_marks:
            words[i] = words[i][:-1]
        words[i] = words[i].lower()

    for word in words:
        flag = 0
        for symbol in word:
            if ('A' <= symbol <= 'Z') or ('a' <= symbol <= 'z'):
                pass
            else:
                flag = 1
                break
        if flag == 0:
            if word not in answer:
                answer[word] = 1
            else:
                answer[word] += 1

    return answer


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """

    # пиши свой код здесь
    for i, item in enumerate(numbers):
        for j in range(exp - 1):
            numbers[i] = numbers[i] * item

    return numbers


def get_cashback(operations: List[Dict[str, Any]], special_category: List[str]) -> float:
    """
    Функция для расчета кешбека по операциям.
    За покупки в обычных категориях возвращается 1% от стоимости покупки
    За покупки в special_category начисляют 5% от стоимости покупки

    :param operations: список словарей, содержащих поля
           amount - сумма операции
           category - категория покупки
    :param special_category: список категорий повышенного кешбека
    :return: размер кешбека
    """

    res = 0
    for x in operations:
        if x['category'] in special_category:
            res += x['amount'] * 0.05
        else:
            res += x['amount'] * 0.01
    return res


def get_path_to_file() -> Optional[Path]:
    """
    Находит корректный путь до тестового файла.

    Если запускать тесты из pycharm - начальная папка - tests
    Если запускать файлы через make tests - начальная папка - корень проекта

    :return: путь до тестового файла tasks.csv
    """
    if Path().resolve().name == 'tests':
        base_path = Path().resolve().parent
    else:
        base_path = Path().resolve()
    return base_path / 'tasks' / 'practice3' / 'tasks.csv'


def csv_reader(header: str) -> int:
    """
    Функция считывает csv файл и подсчитывает количество
    уникальных элементов в столбце.
    Столбец выбирается на основе имени заголовка,
    переданного в переменной header.

    Обратите внимание на структуру файла!
    Первая строка - строка с заголовками.
    Остальные строки - строки с данными.

    Файл для анализа: tasks.csv
    Для того чтобы файл корректно открывался в тестах:
    для получения пути до файла - используйте функцию get_path_to_file
    которая определена перед функцией.

    CSV анализируем с помощью встроенной библиотеки csv

    :param header: название заголовка
    :return: количество уникальных элементов в столбце
    """

    # пиши свой код здесь
    dct = set()
    index: int
    with open(get_path_to_file()) as csv_file:
        file = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(file):
            if i == 0:
                for j, item in enumerate(row):
                    if item == header:
                        index = j
            else:
                dct.add(row[index])

    return len(dct)
