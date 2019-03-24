from requests import get
import json
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


class GharageNewsClient(object):

    def __init__(self):
        self.site_url = 'https://gharage.com/'

    def get_news(self, page=1):
        url = self.site_url + 'page/{}/'.format(page)
        try:
            with closing(get(url, stream=True)) as response:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Selecting all article elements that have 'post', 'type-post' and 'status-publish' as part of their classes
                articles = soup.find_all(
                    'article',
                    {
                        'class': lambda x: x
                        and set(['post', 'type-post', 'status-publish']).issubset(x.split())
                    })

                result = []

                # Looping through found articles and getting data out of the html elements
                for article in articles:
                    data = {}

                    data['title'] = article.find(
                        'h2', class_='entry-title').a.text

                    data['author'] = article.find(
                        'span', class_="author vcard").a.text

                    data['author_url'] = article.find(
                        'span', class_="author vcard").a['href']

                    data['post_image'] = article.find('img')['src']

                    data['post_time'] = article.find(
                        'time', 
                        {
                            'class': lambda x: x and set(['entry-date', 'published']).issubset(x.split())
                        }).text

                    data['post_detail'] = str(article.find(
                        'div', class_="entry-excerpt").text).strip()

                    result.append(data)

                return json.dumps(result)
        except RequestException as cause:
            print(cause)
