from flask import Flask, Response, request
from gharage import GharageNewsClient

app = Flask(__name__)
client = GharageNewsClient()


@app.route("/")
def hello():
    # Getting the page number from the request
    pageNumber = request.args.get('page')

    if pageNumber is not None and int(pageNumber) is not None:
        news = client.get_news(page=pageNumber)
    else:
        news = client.get_news()
    resp = Response(news, status=200, mimetype='application/json')
    return resp


if __name__ == "__main__":
    app.run()
