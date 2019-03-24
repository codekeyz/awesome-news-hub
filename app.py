from flask import Flask, Response
from gharage import GharageNewsClient

app = Flask(__name__)

@app.route("/")
def hello():
  news = GharageNewsClient().get_news()
  resp = Response(news, status=200, mimetype='application/json')
  return resp

if __name__ == "__main__":
  app.run()