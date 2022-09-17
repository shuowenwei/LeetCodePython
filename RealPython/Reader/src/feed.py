# feed.py

from functools import cache

import feedparser
import html2text

import reader

@cache
def _get_feed(url=reader.URL):
    """Read the web feed, use caching to only read it once"""
    return feedparser.parse(url)

def get_site(url=reader.URL):
    """Get name and link to website of the feed"""
    feed = _get_feed(url).feed
    return f"{feed.title} ({feed.link})"

def get_titles(url=reader.URL):
    """List titles in the feed"""
    articles = _get_feed(url).entries
    return [a.title for a in articles]

def get_article(article_id, url=reader.URL):
    """Get article from feed with the given ID"""
    articles = _get_feed(url).entries
    article = articles[int(article_id)]
    html = article.content[0].value
    text = html2text.html2text(html)
    return f"# {article.title}\n\n{text}"

