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

    #speach = Speach()
    #speach.text_to_speach()
