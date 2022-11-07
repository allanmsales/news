import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

def head_line(url, soup_function):
    page = http.request('GET', url)
    soup = BeautifulSoup(page.data, 'html.parser') 
    return eval(soup_function)

class Portal():
    def __init__(self, name, url, soup_function):
        self.name = name
        self.url = url
        self.soup_function = soup_function

    def head_line(self):
        page = http.request('GET', self.url)
        soup = BeautifulSoup(page.data, 'html.parser') 
        return eval(self.soup_function)

    def print(self):
        print(self.name + ': ', self.head_line())

### UOL ###
uol = Portal('UOL', 'https://www.uol.com.br', 'soup.find("h3", {"class": "title__element"}).text')
uol.print()

### R7 ###
r7 = Portal('R7', 'https://www.r7.com/', 'soup.find("a", {"class": "r7-flex-title-h3__link"}).text')
r7.print()

### VALOR ###
valor = Portal('VALOR', 'https://valor.globo.com/', 'soup.find("a", {"class": "bstn-dedupe-url"}).text')
valor.print()

### INFOMONEY ###
infomoney = Portal('INFOMONEY', 'https://www.infomoney.com.br/', 'soup.find("a", {"class": "cover-link"})["title"]')
infomoney.print()

### FOLHA DE SP ###
folha_de_sp = Portal('FOLHA DE SP', 'https://www.folha.uol.com.br/', 'soup.find("h2", {"class": "c-main-headline__title"}).text')
folha_de_sp.print()

### JOVEM PAN ###
jovem_pan = Portal('JOVEM PAN', 'https://jovempan.com.br/', 'soup.find("h2", {"class": "title"}).text')
jovem_pan.print()

### CNN BRASIL ###
cnn_brasil = Portal('CNN BRASIL', 'https://www.cnnbrasil.com.br/', 'soup.find("h2", {"class": "home__title headline__primary_title"}).text')
cnn_brasil.print()

### DIÁRIO DO NORDESTE ###
diario_do_nordeste = Portal('DIÁRIO DO NORDESTE', 'https://diariodonordeste.verdesmares.com.br/', 'soup.find("h2", {"class": "m-c-teaser__heading"}).text')
diario_do_nordeste.print()

### THE NEW YORK TIMES ###
the_new_york_times = Portal('THE NEW YORK TIMES', 'https://www.nytimes.com/', 'soup.find("h3", {"class": "indicate-hover"}).text')
the_new_york_times.print()

### THE WASHINGTON POST ###
the_washington_post = Portal('THE WASHINGTON POST', 'https://www.washingtonpost.com/', 'soup.find("h2", {"class": "relative left font--headline font-bold font-size-xl"}).text')
the_washington_post.print()

### FRANCE 24 ###
france_24 = Portal('FRANCE 24', 'https://www.france24.com/fr/', 'soup.find("p", {"class": "article__title"}).text')
france_24.print()

### REUTERS ###
reuters = Portal('REUTERS', 'https://www.reuters.com/', 'soup.find("div", {"class": "media-story-card__header__1NpsG"}).text')
reuters.print()

### CNN ### RETURNS NOTHING
'''
reuters = Portal('CNN', 'https://edition.cnn.com/', 'soup.find("article", {"class": "cd"})')
reuters.print()
'''

### ESTADO DE SP ### BLOQUED
'''
valor = Portal('ESTADO DE SP', 'https://www.estadao.com.br/', 'page.data')
valor.print()
'''

### G1 ### HASHED
'''
valor = Portal('G1', 'https://g1.globo.com/', 'page.data')
valor.print()
'''
