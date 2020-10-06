# Импорт всех нужных модулей
import requests
from bs4 import BeautifulSoup

# Главный класс
class Url():
    # Конструктор и инициализатор
    def __init__(self, url, user_agent=None):
        self.url = url
        """
        User Agent - это штука, с помощью которой браузер думает, что мы не бот.
        Узнать свой юзер агент можно узнать на https://www.whatsmyua.info/
        """
        if user_agent is None:
            self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        else:
            self.user_agent = user_agent

        self.headers = {
            'User-Agent': self.user_agent
        }

    # Функция парсинга должна принимать такие аргументы, как класс части сайта и тег(как пример, класс price, а тег div)
    def parse(self, meta_class, tag):
        self.urlResponse = requests.get(url=self.url, headers=self.headers)
        self.soupUrl = BeautifulSoup(self.urlResponse.content, 'html.parser')
        self.parsed = self.soupUrl.find_all(tag, class_=meta_class)
        self.parsedArray = []
        self.parsedText = ''
        # В массив передаются все текстовые элементы с указанным ранее тегом
        for i in self.parsed:
            self.parsedArray.append(i.getText(strip=True))
        index = 0
        # Перенос всех элементов массивва в единую строку
        for i in self.parsedArray:
            self.parsedText = self.parsedText + " " + self.parsedArray[index]
            index += 1
        # Возращение текста
        return self.parsedText
