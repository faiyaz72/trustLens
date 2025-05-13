import logging
from collections import defaultdict
from textblob import TextBlob

from app.core.claim_verbs import get_claim_verbs
from app.core.fact_check import build_search_query, fact_check_claim
from app.core.nlp import get_spacy_model
from app.utils.constants import ENITITY_ANALYSIS_LOOKUP, CLAIM_ENTITY_LOOKUP
from app.utils.fuzzy import normalize_string
from app.utils.utils import clean_text, extract_article
from app.core.sentimental_verbs import SENTIMENTAL_VERBS

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

CLAIM_VERBS = get_claim_verbs()

def article_detail(url: str):
    logging.info(f"Fetching article details from URL: {url}")
    article = extract_article(url)
    return {
        "title": article.title,
        "text": article.text[:500],
        "author": article.authors,
        "publish_date": str(article.publish_date) if article.publish_date else None,
        "url": article.url
    }


def analyze_article(url: str):
    
    logging.info(f"Analyzing article from URL: {url}")
    article = extract_article(url)
    analysis = generate_entity_analysis(article.text)
    return {
        "title": article.title,
        "author": article.authors,
        "publish_date": str(article.publish_date) if article.publish_date else None,
        "analysis": analysis,
    }

def is_entity_target_of_sentiment(sentence, entity_span):
    """
    Determine if the entity is the grammatical subject or object
    of an emotionally loaded verb in the sentence.
    """
    for token in sentence:
        if token.dep_ in ("nsubj", "dobj", "pobj") and token.text.lower() in entity_span.text.lower():
            # Optional: Check if the governing verb is emotionally strong
            head_verb = token.head
            if head_verb.pos_ == "VERB":
                # Simple check: verbs like 'support', 'hate', 'criticize', etc.
                if head_verb.lemma_.lower() in SENTIMENTAL_VERBS:
                    return True
                else:
                    return True  # For now, be permissive
    return False

def generate_entity_analysis(text):
    nlp = get_spacy_model()
    doc = nlp(text)

    sentences = list(doc.sents)
    sentiment_dict = defaultdict(list)
    claim_sentences = []

    for idx, sentence in enumerate(sentences):
        for ent in sentence.ents:
            relevant_sentences = sentences[max(idx-1, 0) : min(idx+2, len(sentences))]
            if ent.label_ in ENITITY_ANALYSIS_LOOKUP:
                if (is_entity_target_of_sentiment(sentence, ent)):
                    relavant_text = " ".join([clean_text(sent) for sent in relevant_sentences])
                    normalized = normalize_string(ent.text)
                    blob = TextBlob(relavant_text)
                    sentiment_dict[normalized].append((blob.sentiment.polarity, blob.sentiment.subjectivity))
        if filter_sentence_claim(sentence):
            claim_object = {
                "claim": clean_text(sentence),
                "score": fact_check_claim(clean_text(sentence)),
                "entities": get_entities(sentence),
            }
            claim_sentences.append(claim_object)
                    
    
    average_sentiment = calculate_average_sentiment(sentiment_dict)
    return {
        "average_sentiment": average_sentiment,
        "claim_sentences": claim_sentences
    }

def get_entities(sentence):
    """
    Extract entities from the sentence and return them in a dictionary.
    """
    entities = []
    for ent in sentence.ents:
        if ent.label_ in ENITITY_ANALYSIS_LOOKUP:
            normalized = normalize_string(ent.text)
            if normalized not in entities:
                entities.append(normalize_string(ent.text))
    return entities

def is_entity_target_of_sentiment(sentence, entity_span):
    """
    Determine if the entity is the grammatical subject or object
    of an emotionally loaded verb in the sentence.
    """
    for token in sentence:
        if token.text.lower() in entity_span.text.lower() and token.dep_ in ("nsubj", "dobj", "pobj"):
            head_verb = token.head
            if head_verb.pos_ == "VERB":
                return True
    return False

def filter_sentence_claim(sentence):
    """
    Check if the sentence contains a claim verb.
    """
    valid_ent: bool = False
    for ent in sentence.ents:
        if ent.label_ in CLAIM_ENTITY_LOOKUP:
            valid_ent = True
            break

    if not valid_ent:
        return False
    
    for token in sentence:
        if token.pos_ == "VERB" and token.lemma_.lower() in CLAIM_VERBS:
            return True
    return False


def calculate_average_sentiment(sentiment_dict):
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
        
    return average_sentiment
