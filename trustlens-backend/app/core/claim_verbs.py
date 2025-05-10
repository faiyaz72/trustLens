CLAIM_VERBS = {

    # --- Assertion / Reporting ---
    "say", "state", "report", "claim", "announce", "declare", "assert", "affirm",
    "proclaim", "mention", "describe", "clarify", "explain", "reveal", "disclose",
    "expose", "communicate", "testify", "chronicle", "narrate", "note", "observe",
    "acknowledge", "admit", "concede", "document", "publish", "uncover", "inform",
    "depict", "portray", "highlight", "illustrate", "outline", "detail", "record",
    "relate", "share", "show", "tell", "exemplify", "stress",

    # --- Suggestion / Proposal / Advocacy ---
    "suggest", "recommend", "propose", "advocate", "encourage", "urge", "plead",
    "advice", "call for", "press for", "push for", "lobby for", "campaign for",
    "petition", "support", "back", "stand by", "promote", "endorse", "argue for",

    # --- Warning / Prediction / Estimation ---
    "warn", "forecast", "predict", "anticipate", "estimate", "speculate",
    "expect", "envision", "prepare", "project", "foresee", "caution", "alert",
    "signal", "suspect", "hint", "imply", "guess", "assume", "extrapolate",

    # --- Criticism / Attack / Denial ---
    "criticize", "attack", "oppose", "dispute", "deny", "refute", "rebut",
    "reject", "question", "contest", "dismiss", "decry", "condemn", "ridicule",
    "mock", "challenge", "undermine", "debate", "counter", "cast doubt on",
    "rebuff", "repudiate", "repulse", "defy", "protest", "object", "oppose",
    "clash", "feud", "fight against", "rail against",

    # --- Accusation / Allegation / Blame ---
    "accuse", "blame", "charge", "allege", "implicate", "fault", "condemn",
    "denounce", "indict", "attribute", "warn against", "call out", "name",
    "point finger at", "assert wrongdoing by",

    # --- Support / Agreement / Defense ---
    "defend", "uphold", "justify", "reinforce", "maintain", "stand up for",
    "approve", "validate", "confirm", "ratify", "strengthen", "align with",
    "endorse", "favor", "side with", "second", "authorize", "legitimize",

    # --- Quantification / Measurement / Analysis ---
    "measure", "assess", "analyze", "survey", "scrutinize", "evaluate", "calculate",
    "examine", "study", "explore", "research", "investigate", "inspect",
    "compare", "correlate", "audit", "review", "track", "map", "trace",
    "monitor", "check", "estimate", "quantify", "tally", "count", "certify",

    # --- Belief / Thought / Hypothesis ---
    "believe", "think", "feel", "assume", "suspect", "hold", "theorize",
    "hypothesize", "doubt", "conclude", "perceive", "presume", "consider",
    "speculate about", "suppose", "visualize", "imagine", "ponder",

    # --- Emphasis / Highlighting / Amplification ---
    "stress", "emphasize", "underscore", "reiterate", "underline",
    "reaffirm", "reassert", "restate", "accentuate", "draw attention to",
    "shine a light on", "spotlight", "focus on", "zoom in on",

    # --- Demanding / Requesting / Calling for Action ---
    "request", "demand", "call for", "ask for", "plead for", "seek",
    "press for", "lobby", "petition for", "appeal for", "solicit",
    "campaign for", "urge action", "implore",

    # --- Apology / Acknowledgement of Mistakes ---
    "apologize", "regret", "confess", "admit error", "acknowledge fault",
    "concede mistake", "own up", "accept responsibility", "express regret",

    # --- Agreement / Cooperation / Consent ---
    "agree", "consent", "comply", "collaborate", "coordinate", "align",
    "concur", "ratify", "approve", "endorse jointly", "commit to", "ally with",

    # --- Enforcement / Imposition / Regulation ---
    "enforce", "impose", "mandate", "order", "command", "decree",
    "authorize", "legislate", "govern", "administer", "regulate",
    "enact", "institute", "inaugurate",

    # --- Funding / Resource Allocation / Donation ---
    "fund", "finance", "subsidize", "allocate", "invest", "sponsor",
    "donate", "contribute", "grant", "budget", "endow", "devote resources",
    "pledge funding",

    # --- Event / Incident Reporting ---
    "host", "organize", "celebrate", "mark", "commemorate", "launch",
    "announce", "coordinate", "initiate", "stage", "schedule", "plan",
    "present", "open", "lead", "spearhead",

    # --- Misc Additional ---
    "allude to", "broach", "hint at", "bring up", "touch on", "raise", "reference",
    "frame", "paint", "characterize", "portray", "depict", "highlight", "dramatize",
    "sensationalize", "glorify", "vilify", "stigmatize", "amplify", "magnify",
    "downplay", "obfuscate", "cover up", "misrepresent", "misstate"
}

def get_claim_verbs():
    """
    Returns a set of verbs that are commonly associated with claims.
    """
    return CLAIM_VERBS