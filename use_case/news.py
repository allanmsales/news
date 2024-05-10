from entity.headlines.uol import Uol
from entity.headlines.r7 import R7
from entity.headlines.valor import Valor
from entity.headlines.infomoney import Infomoney
from entity.headlines.folha_de_sp import FolhaDeSp
from entity.headlines.jovem_pan import JovemPan
from entity.headlines.diario_do_nordeste import DiarioDoNordeste
from entity.headlines.cnn_brasil import CnnBrasil
from entity.headlines.the_new_york_times import TheNewYorkTimes
from entity.headlines.the_washington_post import TheWashigtonPost
from entity.headlines.usa_today import UsaToday
from entity.headlines.fox_news import FoxNews
from entity.headlines.nbc_news import NbcNews
from entity.headlines.bloomberg import Bloomberg
from entity.headlines.news_week import NewsWeek
from entity.headlines.bbc import Bbc
from entity.headlines.france_24 import France24
from entity.speach.speach import Speach

from bs4 import BeautifulSoup 
import requests 
import re 


def news_pipeline():
    '''
    uol = Uol()
    print(uol.summary)
    #r7 = R7()
    #print(r7.summary)
    valor = Valor()
    print(valor.summary)
    infomoney = Infomoney()
    print(infomoney.summary)
    folha_de_sp = FolhaDeSp()
    print(folha_de_sp.summary)
    jovem_pan = JovemPan()
    print(jovem_pan.summary)
    diario_do_nordeste = DiarioDoNordeste()
    print(diario_do_nordeste.summary)
    cnn_brasil = CnnBrasil()
    print(cnn_brasil.summary)
    france_24 = France24()
    print(france_24.summary)
    '''
    the_new_york_times = TheNewYorkTimes()
    the_washington_post = TheWashigtonPost()
    usa_today = UsaToday()
    fox_news = FoxNews()
    nbc_news = NbcNews()
    bloomberg = Bloomberg()
    news_week = NewsWeek()
    bbc = Bbc()

    summary = [
        #uol.summary,
        #r7.summary,
        #valor.summary,
        #infomoney.summary,
        #folha_de_sp.summary,
        #jovem_pan.summary,
        #diario_do_nordeste.summary,
        #cnn_brasil.summary,
        #the_new_york_times.summary,
        #the_washington_post.summary,
        #usa_today
        #france_24.summary
    ]

    summary = ' '.join(summary)

    #speach = Speach(summary)
    #speach.text_to_speach()

    return summary