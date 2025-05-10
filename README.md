# TrustLens API

**TrustLens** is an intelligent article analyzer designed to assist with news verification, sentiment analysis, and claim extraction.

Given a URL to an article, TrustLens performs:

* **Entity-focused sentiment analysis**: Detects key named entities (e.g., countries, organizations, persons) and evaluates the emotional tone around them.
* **Claim extraction**: Identifies factual statements that could be independently fact-checked.

This project aims to support fake news detection, bias analysis, and building credibility scores for news content.

---

## Features

* ✅ Extracts **key named entities**.
* ✅ Analyzes **average sentiment** (polarity and subjectivity) per entity.
* ✅ Detects **factual claims** and associates them with entities.
* ✅ Provides a clean, structured JSON response ready for further analysis.

---

## API Endpoint: `/analyse`

**Request:**

```bash
POST /analyse
Content-Type: application/json

{
  "url": "https://www.bbc.com/news/articles/cvg9d913v20o"
}
```

**Response Example:**

```json
{
  "title": "India and Pakistan accuse each other of 'violations' after ceasefire deal",
  "author": [],
  "publish_date": null,
  "analysis": {
    "average_sentiment": {
      "INDIAN": {
        "average_polarity": -0.0576,
        "average_subjectivity": 0.2171
      },
      "VIKRAM MISRI": {
        "average_polarity": 0.0,
        "average_subjectivity": 0.2793
      },
      "PAKISTAN": {
        "average_polarity": 0.1063,
        "average_subjectivity": 0.3660
      },
      "DONALD TRUMP'S": {
        "average_polarity": 0.1917,
        "average_subjectivity": 0.3083
      }
    },
    "claim_sentences": [
      {
        "claim": "India and Pakistan accuse each other of 'violations' after ceasefire deal 2 hours ago Share",
        "score": 0,
        "entities": ["INDIAN", "PAKISTAN"]
      },
      {
        "claim": "After sounds of explosions were heard in Indian-administered Kashmir, India's Foreign Secretary Vikram Misri said there had been 'repeated violations of the understanding we arrived at'.",
        "score": 0,
        "entities": ["INDIAN", "VIKRAM MISRI"]
      },
      {
        "claim": "A short while later, Pakistan's foreign ministry said it remained 'committed to faithful implementation of a ceasefire... notwithstanding the violations being committed by India in some areas'.",
        "score": 0,
        "entities": ["PAKISTAN", "INDIAN"]
      },
      {
        "claim": "The use of drones, missiles and artillery started when India struck targets in Pakistan and Pakistan-administered Kashmir in response to a deadly militant attack in Pahalgam last month.",
        "score": 0,
        "entities": ["INDIAN", "PAKISTAN", "PAHALGAM"]
      },
      {
        "claim": "US President Donald Trump announced the news on his Truth Social Platform on Saturday morning.",
        "score": 0,
        "entities": ["WHITE HOUSE", "DONALD TRUMP'S"]
      }
      // ... (Additional claims extracted)
    ]
  }
}
```

---

## Key Field Explanations

| Field                        | Description                                                                                                              |
| :--------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| `title`                      | Title of the article.                                                                                                    |
| `author`                     | List of detected authors (if available).                                                                                 |
| `publish_date`               | Detected publication date (if available).                                                                                |
| `analysis.average_sentiment` | Dictionary showing each major entity and its average polarity (sentiment positivity) and subjectivity (fact vs opinion). |
| `analysis.claim_sentences`   | List of factual claim sentences with associated entities. Useful for fact-checking and trust scoring.                    |

---

## Future Enhancements

* Fact-checking claims against external knowledge bases.
* Assigning credibility/confidence scores to claims.
* Entity normalization and canonical mapping.
* Bias analysis through polarity spread detection.

---

## Setup and Run

(Setup instructions for FastAPI / Uvicorn if required will be placed here in future updates.)

---

## License

This project is for educational and research purposes.

---

**Developed as part of a broader initiative to combat misinformation and enhance news credibility analysis.**
