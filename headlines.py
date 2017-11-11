# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask  import  Flask
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
    first_article = feed['entries'][0]
    return """<html>
      <body>
           <h1>china headlines</h1>
           <b>{0}</b>
           <i>{1}</i>
           <p>{2}</p>
      </body>
      </html>""".format(first_article.get("title"),
                        first_article.get('published'),
                        first_article.get("summary"))


if __name__ == "__main__":
    app.run(debug=True)