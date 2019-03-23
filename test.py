from gharage import GharageNewsClient

client = GharageNewsClient()

news = client.get_news()

print(news)