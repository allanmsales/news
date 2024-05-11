import config
from entity.headlines.the_new_york_times import TheNewYorkTimes
from entity.headlines.the_washington_post import TheWashigtonPost
from entity.headlines.usa_today import UsaToday
from entity.headlines.fox_news import FoxNews
from entity.headlines.nbc_news import NbcNews
from entity.headlines.bloomberg import Bloomberg
from entity.headlines.news_week import NewsWeek
from entity.headlines.bbc import Bbc
from langchain_openai import ChatOpenAI


def check_subject(headline):
    llm = ChatOpenAI(api_key=config.OPENAI_API_KEY)
    response = llm.invoke(f'Answer YES or NO if this content: {headline} is related to politics.')
    return response.content

def summary():
    the_new_york_times = TheNewYorkTimes()
    the_washington_post = TheWashigtonPost()
    usa_today = UsaToday()
    fox_news = FoxNews()
    nbc_news = NbcNews()
    bloomberg = Bloomberg()
    news_week = NewsWeek()
    bbc = Bbc()

    print(f'{check_subject(the_new_york_times.head_line)}')
    print(f'{check_subject(the_washington_post.head_line)}')
    print(f'{check_subject(usa_today.head_line)}')
    print(f'{check_subject(fox_news.head_line)}')
    print(f'{check_subject(nbc_news.head_line)}')
    print(f'{check_subject(bloomberg.head_line)}')
    print(f'{check_subject(news_week.head_line)}')
    print(f'{check_subject(bbc.head_line)}')

    return ''