from entity.headlines.portal import Portal
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
from entity.headlines.france_24 import France24
from entity.speak.speak import Speak


def news_pipeline():
    Uol()
    R7()
    Valor()
    Infomoney()
    FolhaDeSp()
    JovemPan()
    DiarioDoNordeste()
    CnnBrasil()
    TheNewYorkTimes()
    TheWashigtonPost()
    France24()

    #speak = Speak()
    #speak.text_to_speach()


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

