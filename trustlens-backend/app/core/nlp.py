import spacy

# Load only once at server startup
nlp = spacy.load("en_core_web_sm")

def get_spacy_model():
    return nlp