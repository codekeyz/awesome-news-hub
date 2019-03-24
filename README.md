# Gharage News Client

## A python scraper to fetch news from the [Gharage News Website](https://gharage.com/)


### Usage
```python
from gharage import GharageNewsClient

client = GharageNewsClient()

# Getting news on page 5 of the website
news = client.get_news(page=5)

print(news)

```

### Sample Output
```json
[
  {
    "title": "MTN Launches 4G+ Service  on 4G Its LTE Advanced Technology",
    "author": "Claude Ayitey",
    "author_url": "https://gharage.com/author/a365yitey/",
    "post_image": "https://gharage.com/wp-content/uploads/2019/03/mtn-launches-4g-gharage-250x170.jpg",
    "post_time": "22nd March, 2019",
    "post_detail": "MTN has launched its 4G+ service to provide faster data speeds with widest coverage using 800MHz and 2600MHz for carrier aggregation."
  },
  {
    "title": "Sturta Launches Marketplace With 1000+ Vetted Professionals",
    "author": "Claude Ayitey",
    "author_url": "https://gharage.com/author/a365yitey/",
    "post_image": "https://gharage.com/wp-content/uploads/2019/03/sturta-launches-marketplace-1000-vetted-professionals-gharage-250x170.jpg",
    "post_time": "21st March, 2019",
    "post_detail": "Sturta, a local marketplace for service providers across Africa, has launched with more than 1000 vetted professionals in Accra, Ghana."
  }
]
```

```
If you prefer to use HTTP Calls, make your request to https://gharage-news.herokuapp.com/
```

Feel free to use and submit PR's to improve usage. 