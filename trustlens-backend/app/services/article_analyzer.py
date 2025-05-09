import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from app.utils.extractor import extract_article

def article_detail(url: str):
    logging.info(f"Fetching article details from URL: {url}")
    article = extract_article(url)
    return {
        "title": article.title,
        "author": article.authors,
        "publish_date": str(article.publish_date) if article.publish_date else None,
        "url": article.url
    }


def analyze_article(url: str):
    logging.info(f"Analyzing article from URL: {url}")
    article = extract_article(url)
    return {
        "title": article.title,
        "text": article.text[:500],
        "author": article.authors,
        "publish_date": str(article.publish_date) if article.publish_date else None
    }