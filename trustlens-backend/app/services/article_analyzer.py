from app.utils.extractor import extract_article

def analyze_article(url: str):
    article = extract_article(url)
    return {
        "title": article.title,
        "text": article.text[:500],
        "author": article.authors,
        "publish_date": str(article.publish_date) if article.publish_date else None
    }