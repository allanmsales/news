from entity.portal import Portal
from entity.uol import Uol
from entity.r7 import R7


def news_pipeline():
    uol = Uol()
    #r7 = R7()
    
    ### R7 ###
    try:
        r7 = Portal(
            'R7',
            'https://www.r7.com/',
            'soup.find("a", {"class": "r7-flex-title-h3__link"}).text'
            )
        r7.print()
    except:
        print('Impossible to read ' + r7.name)
    
    ### VALOR ###
    try:
        valor = Portal(
            'VALOR',
            'https://valor.globo.com/',
            'soup.find("a", {"class": "bstn-dedupe-url"}).text'
            )
        valor.print()
    except:
        print('Impossible to read ' + valor.name)

    ### INFOMONEY ###
    try:
        infomoney = Portal(
            'INFOMONEY',
            'https://www.infomoney.com.br/',
            'soup.find("a", {"class": "cover-link"})["title"]'
            )
        infomoney.print()
    except:
        print('Impossible to read ' + infomoney.name)

    ### FOLHA DE SP ###
    try:
        folha_de_sp = Portal(
            'FOLHA DE SP',
            'https://www.folha.uol.com.br/',
            'soup.find("h2", {"class": "c-main-headline__title"}).text'
            )
        folha_de_sp.print()
    except:
        print('Impossible to read ' + folha_de_sp.name)

    ### JOVEM PAN ###
    try:
        jovem_pan = Portal(
            'JOVEM PAN',
            'https://jovempan.com.br/',
            'soup.find("h2", {"class": "title"}).text'
            )
        jovem_pan.print()
    except:
        print('Impossible to read ' + jovem_pan.name)

    ### CNN BRASIL ###
    try:
        cnn_brasil = Portal(
            'CNN BRASIL',
            'https://www.cnnbrasil.com.br/',
            'soup.find("h2", {"class": "home__title headline__primary_title"}).text'
            )
        cnn_brasil.print()
    except:
        print('Impossible to read ' + cnn_brasil.name)

    ### DIÁRIO DO NORDESTE ###
    try:
        diario_do_nordeste = Portal(
            'DIÁRIO DO NORDESTE',
            'https://diariodonordeste.verdesmares.com.br/',
            'soup.find("h2", {"class": "m-c-teaser__heading"}).text'
            )
        diario_do_nordeste.print()
    except:
        print('Impossible to read ' + diario_do_nordeste.name)

    ### THE NEW YORK TIMES ###
    try:
        the_new_york_times = Portal(
            'THE NEW YORK TIMES',
            'https://www.nytimes.com/',
            'soup.find("h3", {"class": "indicate-hover"}).text'
            )
        the_new_york_times.print()
    except:
        print('Impossible to read ' + the_new_york_times.name)

    ### THE WASHINGTON POST ###
    try:
        the_washington_post = Portal(
            'THE WASHINGTON POST',
            'https://www.washingtonpost.com/',
            'soup.find("h2", {"class": "relative left font--headline font-bold font-size-xl"}).text'
            )
        the_washington_post.print()
    except:
        print('Impossible to read ' + the_washington_post.name)

    ### FRANCE 24 ###
    try:
        france_24 = Portal(
            'FRANCE 24',
            'https://www.france24.com/fr/',
            'soup.find("p", {"class": "article__title"}).text'
            )
        france_24.print()
    except:
        print('Impossible to read ' + france_24.name)


    ### REUTERS ###
    try:
        reuters = Portal(
            'REUTERS',
            'https://www.reuters.com/',
            'soup.find("div", {"class": "media-story-card__header__1NpsG"}).text'
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

