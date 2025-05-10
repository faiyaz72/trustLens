from newspaper import Article

def extract_article(url: str):
    article = Article(url)
    article.download()
    article.parse()
    return article

def clean_text(sentence):
    """
    Clean the text of sentences by removing unnecessary whitespace
    and normalizing the text.
    """
    return sentence.text.replace("\\", "").replace("\n", " ").replace("\r", " ").replace("\t", " ").strip()
    