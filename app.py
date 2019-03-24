from flask import Flask, jsonify
from gharage import GharageNewsClient

app = Flask(__name__)

@app.route("/")
def hello():
  news = GharageNewsClient().get_news()
  resp = jsonify(news)
  return resp

if __name__ == "__main__":
  app.run()