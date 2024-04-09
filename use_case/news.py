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
from entity.speach.speach import Speach


def news_pipeline():
    uol = Uol()
    print(uol.summary)
    #r7 = R7()
    #print(r7.summary)
    valor = Valor()
    infomoney = Infomoney()
    folha_de_sp = FolhaDeSp()
    jovem_pan = JovemPan()
    diario_do_nordeste = DiarioDoNordeste()
    cnn_brasil = CnnBrasil()
    the_new_york_times = TheNewYorkTimes()
    the_washington_post = TheWashigtonPost()
    france_24 = France24()

    summary = [
        uol.summary,
        #r7.summary,
        valor.summary,
        infomoney.summary,
        folha_de_sp.summary,
        jovem_pan.summary,
        diario_do_nordeste.summary,
        cnn_brasil.summary,
        the_new_york_times.summary,
        the_washington_post.summary,
        france_24.summary
    ]

    summary = ' '.join(summary)

    speach = Speach(summary)
    speach.text_to_speach()
