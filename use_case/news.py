from entity.portal import Portal
from entity.uol import Uol
from entity.r7 import R7
from entity.valor import Valor
from entity.infomoney import Infomoney
from entity.folha_de_sp import FolhaDeSp
from entity.jovem_pan import JovemPan
from entity.diario_do_nordeste import DiarioDoNordeste
from entity.cnn_brasil import CnnBrasil


def news_pipeline():
    Uol()
    R7()
    Valor()
    Infomoney()
    FolhaDeSp()
    JovemPan()
    DiarioDoNordeste()
    CnnBrasil()


    ### THE NEW YORK TIMES ###
    try:
        the_new_york_times = Portal(
            'THE NEW YORK TIMES',
            'https://www.nytimes.com/',
            'soup.find("p", {"class": "indicate-hover"}).text'
            )
        the_new_york_times.print()
    except:
        print('Impossible to read ' + the_new_york_times.name)

    ### THE WASHINGTON POST ###
    try:
        the_washington_post = Portal(
            'THE WASHINGTON POST',
            'https://www.washingtonpost.com/',
            'soup.find("div", {"class": "headline relative gray-darkest pb-xs"}).text'
            )
        the_washington_post.print()
    except:
        print('Impossible to read ' + the_washington_post.name)

    ### FRANCE 24 ###
    try:
        france_24 = Portal(
            'FRANCE 24',
            'https://www.france24.com/fr/',
            'soup.find("div", {"class": "article__title"}).text'
            )
        france_24.print()
    except:
        print('Impossible to read ' + france_24.name)


    ### REUTERS ###
    try:
        reuters = Portal(
            'REUTERS',
            'https://www.reuters.com/',
            'soup.find("span", {"class": "text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_4__14ZqK heading__base__2T28j heading__heading_4__3yjho"}).text'
            )
        reuters.print()
    except:
        print('Impossible to read ' + reuters.name)


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

    ### NOVA BRASIL ###
    try:
        nova_brasil = Portal(
            'NOVA BRASIL',
            'https://novabrasilfm.com.br/',
            'soup.find_all("div", {"class": "item"})'
            )
        soup = nova_brasil.head_line()
        print(soup.result[9].h2.text)
        print(soup.result[9].a.get("href"))
    except:
        print('Impossible to read ' + nova_brasil.name)

