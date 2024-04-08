import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()


class Portal():
    def __init__(self, name, url, soup_function):
        self.name = name
        self.url = url
        self.soup_function = soup_function
        self.summary = 'TEST'

    def head_line(self):
        page = http.request('GET', self.url)
        soup = BeautifulSoup(page.data, 'html.parser')
        self.result = eval(self.soup_function)
        return self
    
    def print(self):
        self.head_line()
        print(self.name + ': ', self.result.strip() + '.')

    