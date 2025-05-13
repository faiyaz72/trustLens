import logging
from rapidfuzz import process
from app.core.cananical_manager import get_canonical_entities, add_canonical_entity

def normalize_string(s: str) -> str:
    """
    Normalize a string by removing leading and trailing whitespace and converting to lowercase.
    """
    try:
        striped = s.upper().strip()
        result = process.extractOne(
            striped,
            get_canonical_entities(),
            score_cutoff=85
        )

        if result:  # Check if a match was found
            return result[0]
        else:
            add_canonical_entity(striped)
            return striped
    except Exception as e:
        logging.error(f"Error normalizing string: {e}")
        return striped
    
        
   