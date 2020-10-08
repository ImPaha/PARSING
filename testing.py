# Парсинг хабра

# Импортируем библиотеку
from parsing import Url


# Следующие две функции не обязательны, можно просто передавать переменную или значение на прямую
def return_url():
    return 'https://habr.com/ru/'


def return_class():
    return 'post__title_link'


# Создание объекта класс Url
url = Url(return_url())


# Перебор возращаемого массива и вывод результата
for i in url.parse(return_class(), 'a'):
    print(i)