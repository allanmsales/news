from entity.headlines.portal import Portal


class TheWashigtonPost(Portal):
    def __init__(self):
        self.name = 'THE WASHINGTON POST'
        self.url = 'https://www.washingtonpost.com/'
        self.soup_function = 'soup.find("div", {"class": "headline relative gray-darkest pb-xs"}).text'
        super()
        self.save_head_line()
