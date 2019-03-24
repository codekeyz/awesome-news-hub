from gharage import GharageNewsClient

client = GharageNewsClient()

news = client.get_news(page=6)

print(news)