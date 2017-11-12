# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask  import  Flask
from flask import render_template
import feedparser


app = Flask(__name__)

RSS_FEEDS = {'china':'http://news.qq.com/newsgn/rss_newsgn.xml',
             'world':'http://news.qq.com/newsgj/rss_newswj.xml',
             'keji':'http://news.baidu.com/n?cmd=1&class=technnews&tn=rss',
             'edu': 'http://news.baidu.com/n?cmd=1&class=edunews&tn=rss'
             }

@app.route("/")
@app.route("/<published>")
def get_news(published="china"):
    feed=feedparser.parse(RSS_FEEDS[published])
    # first_article = feed['entries'][0]
    return render_template("home.html", articles=feed['entries'])


if __name__ == "__main__":
    app.run(debug=True)