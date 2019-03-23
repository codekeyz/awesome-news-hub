import requests
from bs4 import BeautifulSoup

class GharageNewsClient(object):

    def __init__(self):
        print('Library is now initialized')

    def get_news(self):
        print('Get News from the site')