import urllib3
from bs4 import BeautifulSoup
import requests

http = urllib3.PoolManager()


class AiTechLead():
    def __init__(self):
        self.name = 'AI TECH LEAD'
        self.url = 'https://www.linkedin.com/jobs/search/?currentJobId=3937235151&distance=25.0&geoId=103644278&keywords=AI%20%2B%20TECH%20%2B%20LEAD'
        self.head_line = None
        self.link = None
        self.pipeline()

    def pipeline(self):
        self.get_head_line_and_link()
        #print(self.head_line)
        #print(self.link)

    def get_head_line_and_link(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        self.result = soup.find("ul", {"class": "jobs-search__results-list"})
        self.result = self.result.find_all("li")

        for i in self.result:
            result = i.find("div", {"class": "base-search-card__info"})
            title = result.find("h3", {"class": "base-search-card__title"})
            subtitle = result.find("h4", {"class": "base-search-card__subtitle"})
            meta_data = result.find("span", {"class": "job-search-card__location"})
            link = i.find_all("a")
                        
            print(title.get_text().strip())
            print(subtitle.get_text().strip())
            print(meta_data.get_text().strip())
            print(link[0].get("href"))
            print(f'''#######################
                  
                  ''')
        '''
        news = soup.find_all("a")
        first_news = news[0]
        self.link = f'{self.url}{first_news.get("href")}'
        self.head_line = soup.get_text().strip()
        '''