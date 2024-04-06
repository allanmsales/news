from entity.headlines.portal import Portal


class TheNewYorkTimes(Portal):
    def __init__(self):
        self.name = 'THE NEW YORK TIMES'
        self.url = 'https://www.nytimes.com/'
        self.soup_function = 'soup.find("p", {"class": "indicate-hover"}).text'
        super()
        self.print()
