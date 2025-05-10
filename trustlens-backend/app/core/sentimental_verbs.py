
# This set contains verbs that are commonly associated with positive or negative sentiments.
SENTIMENTAL_VERBS = {
    # Positive Sentiment Verbs
    "support", "praise", "endorse", "admire", "applaud", "commend", "celebrate", "honor", "respect", "value", "appreciate", "welcome", "embrace",
    
    # Negative Sentiment Verbs
    "oppose", "attack", "criticize", "condemn", "reject", "accuse", "denounce", "disparage", "mock", "vilify", "insult", "blame", "question", "target", "punish", "prosecute", "abuse",
    
    # Moderate/Subjective Sentiment Verbs
    "claim", "allege", "suggest", "warn", "advocate", "assert", "defend", "challenge", "debate", "dismiss", "doubt", "fear", "highlight", "stress", "underline", "pressure"
}

def get_sentimental_verbs():
    """
    Returns a set of verbs that are commonly associated with positive or negative sentiments.
    """
    return SENTIMENTAL_VERBS


