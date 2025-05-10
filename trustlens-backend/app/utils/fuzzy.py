from rapidfuzz import process
from app.utils.constants import CANONICAL_ENTITIES

def normalize_string(s: str) -> str:
    """
    Normalize a string by removing leading and trailing whitespace and converting to lowercase.
    """
    try:
        striped = s.upper().strip()
        result = process.extractOne(
            striped,
            CANONICAL_ENTITIES,
            score_cutoff=90
        )

        if result:  # Check if a match was found
            match, score = result
            return match
        else:
            CANONICAL_ENTITIES.append(striped)
            return striped
    except Exception as e:
        print(f"Error normalizing string: {e}")
        return s
    
        
   