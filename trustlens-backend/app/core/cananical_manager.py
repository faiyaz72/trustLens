import os
import json

FILE_PATH = os.path.join(os.path.dirname(__file__), "canonical_entities.json")

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        CANONICAL_ENTITIES = json.load(f)
else:
    CANONICAL_ENTITIES = {}

def save_entities():
    with open(FILE_PATH, "w") as f:
        json.dump(CANONICAL_ENTITIES, f, indent=2)

def get_canonical_entities():
    return CANONICAL_ENTITIES.keys()

def add_canonical_entity(entity):
    if entity not in CANONICAL_ENTITIES:
        CANONICAL_ENTITIES[entity] = ""
        save_entities()