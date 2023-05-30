import requests
import json



def get_news():
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=831499b6e58945babb6d376cf35aa5d4'
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return 'https://newsapi.org/v2/top-headlines?country=in&apiKey=831499b6e58945babb6d376cf35aa5d4'
