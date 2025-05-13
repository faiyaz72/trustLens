# TrustLens API - Article Analysis and Claim Extraction

## Overview

**TrustLens** is an API that analyzes news articles from a given URL and extracts:

* **Average Sentiment Analysis** on key entities (e.g., "Russia", "Zelensky", "Ukraine")
* **Claim Sentences** made in the article
* **Fact-Check Score and Evidence** for each claim using Google Custom Search API

This helps build the foundation for a fully automated **Fact-Checking System**.

---

## Current Features

### 1. Sentiment Analysis

* Extracts named entities (PERSON, GPE, ORG, EVENT, etc.).
* Computes **average polarity** (positive/negative) and **subjectivity** scores for each entity.

### 2. Claim Extraction

* Identifies factual claims made in the article.
* Prioritizes claims involving named entities and strong "claim verbs" (e.g., "announce", "claim", "warn").

### 3. Fact-Checking (Evidence Collection)

* Searches the internet using **Google Custom Search API**.
* Matches the claims against external evidence snippets.
* Assigns a simple score (1 = supported, 0 = unclear) based on fuzzy matching.
* Returns related article snippets as evidence.

---

## Key Fields Explanation

| Field                        | Description                                                             |
| ---------------------------- | ----------------------------------------------------------------------- |
| `title`                      | The title of the analyzed article.                                      |
| `author`                     | List of authors extracted (may be empty).                               |
| `publish_date`               | Date the article was published (nullable).                              |
| `analysis.average_sentiment` | Dictionary where each entity has its average polarity and subjectivity. |
| `analysis.claim_sentences`   | List of detected claims made in the article. Each claim has:            |
| - `claim`                    | Text of the extracted claim sentence.                                   |
| - `score`                    | \[Match Score (0/1), List of Evidence Snippets from Google Search].     |
| - `entities`                 | List of normalized entities detected within the claim.                  |

---

## Sample Output (for `/analyze` endpoint)

```json
{
    "title": "Zelensky challenges Putin to meet him after Trump demands Ukraine-Russia talks",
    "author": [],
    "publish_date": null,
    "analysis": {
        "average_sentiment": {
            "ZELENSKY": {
                "average_polarity": 0.0488,
                "average_subjectivity": 0.4002
            },
            "PUTIN": {
                "average_polarity": 0.0626,
                "average_subjectivity": 0.3268
            },
            "DONALD TRUMP'S": {
                "average_polarity": 0.0600,
                "average_subjectivity": 0.3000
            },
            "UKRAINE": {
                "average_polarity": 0.0470,
                "average_subjectivity": 0.4053
            },
            "TÜrkiye": {
                "average_polarity": 0.0000,
                "average_subjectivity": 0.3000
            },
            "RUSSIA": {
                "average_polarity": 0.0757,
                "average_subjectivity": 0.4129
            }
        },
        "claim_sentences": [
            {
                "claim": "Zelensky challenges Putin to meet him after Trump demands Ukraine-Russia talks",
                "score": [
                    1,
                    [
                        {
                            "title": "Beijing's game of arsenals",
                            "link": "https://thehill.com/opinion/national-security/3877164-beijings-game-of-arsenals/",
                            "snippet": "Munition drain to meet Ukrainian President Volodymyr Zelensky's needs..."
                        },
                        ...
                    ]
                ],
                "entities": [
                    "ZELENSKY",
                    "PUTIN",
                    "UKRAINE",
                    "RUSSIA"
                ]
            },
            ...
        ]
    }
}
```

---

## Project Architecture (High Level)

* **FastAPI** backend
* **spaCy** for NLP (entity extraction, grammar analysis)
* **TextBlob** for sentiment analysis
* **FuzzyWuzzy** for fuzzy string matching
* **Google Custom Search API** for external evidence collection

---

## How to Use

1. **POST** to `/analyze`
2. Provide the **URL** of the article you want to analyze.
3. Receive back structured **sentiment analysis** and **claim verification**.

---

## Future Roadmap

* ✍️ Improve claim matching by semantic embeddings (e.g., SBERT)
* 📊 Score claims by confidence (e.g., \[0-100] instead of 0/1)
* 🛠️ Add entity linking and canonical resolution (e.g., "Donald Trump" == "Trump")
* 🛡️ Fact-check multiple languages (extend spaCy pipelines)

---

## License

MIT License. Free for personal and academic use. Attribution appreciated.

---

## Contributions

PRs and feature ideas welcome! Open an issue if you'd like to collaborate.

---

# 🌟 TrustLens - Bring Transparency to News!
