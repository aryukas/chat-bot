import json
import random
import os
import re
# ----------------------------
# Load intents JSON
# ----------------------------
intents_file = os.path.join(os.path.dirname(__file__), "intents.json")

try:
    with open(intents_file, "r", encoding="utf-8") as f:
        intents = json.load(f)
except FileNotFoundError:
    print(f"Error: '{intents_file}' not found. Make sure it exists.")
    intents = {"intents": []}

# ----------------------------
# Helper functions
# ----------------------------
def preprocess(sentence):
    """
    Tokenize a sentence using regex and lowercase.
    Removes punctuation automatically.
    """
    tokens = re.findall(r'\b\w+\b', sentence.lower())
    return tokens

def predict_intent(message):
    """
    Predict intent based on word overlap with patterns.
    """
    tokens = preprocess(message)
    max_matches = 0
    predicted_tag = "fallback"

    for intent in intents.get('intents', []):
        for pattern in intent.get('patterns', []):
            pattern_tokens = preprocess(pattern)
            matches = len(set(tokens) & set(pattern_tokens))
            if matches > max_matches:
                max_matches = matches
                predicted_tag = intent.get('tag', 'fallback')
    
    return predicted_tag

def get_response(message):
    """
    Return a random response for the predicted intent.
    """
    tag = predict_intent(message)
    for intent in intents.get('intents', []):
        if intent.get('tag') == tag:
            responses = intent.get('responses', [])
            if responses:
                return random.choice(responses)
    # Default fallback
    return "Sorry, I don't understand yet, but I can connect you to support."
