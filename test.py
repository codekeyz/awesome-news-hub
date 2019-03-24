from gharage import GharageNewsClient

client = GharageNewsClient()

# Getting news from page 10 of the site
news = client.get_news(page=40)

print(news)