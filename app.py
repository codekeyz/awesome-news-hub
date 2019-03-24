from flask import Flask
from gharage import GharageNewsClient

app = Flask(__name__)

@app.route("/")
def hello():
  return GharageNewsClient().get_news()

if __name__ == "__main__":
  app.run()