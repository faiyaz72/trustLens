from collections import defaultdict
import logging
from textblob import TextBlob
from app.utils.utils import extract_article
from app.utils.constants import ENITITY_ANALYSIS_LOOKUP
from app.core.nlp import get_spacy_model

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

    generate_entity_analysis(article.text)

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

def generate_entity_analysis(text):
    nlp = get_spacy_model()
    doc = nlp(text)
    entity_set = set()

    for ent in doc.ents:
        if ent.label_ in ENITITY_ANALYSIS_LOOKUP:
            entity_set.add(ent.text)

    sentences = list(doc.sents)
    sentiment_dict = defaultdict(list)

    for sentence in sentences:
        for ent in sentence.ents:
            if ent.text in entity_set:
                blob = TextBlob(sentence.text)
                sentiment_dict[ent.text].append((blob.sentiment.polarity, blob.sentiment.subjectivity))
    
    average_sentiment = {}
    for entity, sentiments in sentiment_dict.items():
        total_polarity = 0 
        total_subjectivity = 0
        for polarity, subjectivity in sentiments:
            total_polarity += polarity
            total_subjectivity += subjectivity
        
        avg_polarity = total_polarity / len(sentiments)
        avg_subjectivity = total_subjectivity / len(sentiments)
    

        average_sentiment[entity] = {
            "average_polarity": avg_polarity,
            "average_subjectivity": avg_subjectivity
        }
    logger.debug(f"Entity analysis result: {average_sentiment}")
    return average_sentiment
