import logging
from textblob import TextBlob
from app.utils.extractor import extract_article
import spacy

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
    blob = TextBlob(article.text)
    sentiment = blob.sentiment

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(article.text)
    for ent in doc.ents:
        print(ent.text, ent.label_)

    logging.debug(f"Sentiment analysis result: {sentiment}")
    return {
        "title": article.title,
        "text": article.text[:500],
        "author": article.authors,
        "publish_date": str(article.publish_date) if article.publish_date else None,
        "sentiment": {
            "polarity": sentiment.polarity,
            "subjectivity": sentiment.subjectivity
        }
    }