import os
import requests
from fuzzywuzzy import fuzz
from app.core.nlp import get_spacy_model
from dotenv import load_dotenv
# import spacy
# nlp = spacy.load("en_core_web_sm")

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

def search_claim(claim_text):
  search_url = "https://www.googleapis.com/customsearch/v1"
  params = {
    "key": GOOGLE_API_KEY,
    "cx": GOOGLE_CSE_ID,
    "q": build_search_query(claim_text),
  }

  response = requests.get(search_url, params=params)
  response.raise_for_status()
  search_results = response.json()

  result = []
  for item in search_results.get("items", []):
      snippet = item.get("snippet")
      title = item.get("title")
      link = item.get("link")
      if snippet:
          result.append({
              "title": (title if title else ""),
              "link": (link if link else ""),
              "snippet": (snippet if snippet else "")
          })
  return result


def build_search_query(claim_text):
    nlp = get_spacy_model()
    doc = nlp(claim_text)
    important_tokens = []
    entity = []
    ENTITY_LABELS = {
        "PERSON", "NORP", "ORG", "GPE", "LOC", "EVENT",
        "DATE", "PERCENT", "MONEY", "QUANTITY"
    }
    for ent in doc.ents:
        if ent.label_ in ENTITY_LABELS:
            entity.append(ent.text)
    for token in doc:
        if token.pos_ in {"NOUN", "VERB", "NUM"} and not token.is_stop:
            important_tokens.append(token.text)
    compressed = list(set(entity + important_tokens))
    search_query = " ".join(compressed)
    return search_query

def evaluate_results(claim_text, query_results):
    """
    Evaluate how well the claim matches external snippets.
    Returns (score, evidence).
    """
    scores = []
    evidence_snippets = []

    for result in query_results:
        match_score = fuzz.partial_ratio(claim_text.lower(), result['snippet'].lower())
        if match_score > 30:  # Threshold can be tuned
            scores.append(match_score)
            evidence_snippets.append(result)

    if not scores:
        return 0, []  # Unclear or no support

    avg_score = sum(scores) / len(scores)
    if avg_score >= 30:
        return 1, evidence_snippets  # Supported
    else:
        return 0, evidence_snippets  # Weak/unclear

def fact_check_claim(claim_text):
    """
    Full fact-checking pipeline for a single claim.
    """
    try:
        snippets = search_claim(claim_text)
        score, evidence = evaluate_results(claim_text, snippets)
        return score, evidence
    except Exception as e:
        print(f"Error during fact checking: {e}")
        return 0, []

if __name__ == "__main__":
    claim = "Western powers called for a 30-day pause in fighting to begin on Monday after European leaders spearheading the so-called \"coalition of the willing\" met in Kyiv on Saturday."
    score, evidence = fact_check_claim(claim)
    # build_search_query(claim)
    print(f"Score: {score}")
    print(f"Evidence: {evidence}")