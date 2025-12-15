import json
import random
import os
import re

# ----------------------------
# File paths
# ----------------------------
BASE_DIR = os.path.dirname(__file__)
INTENTS_FILE = os.path.join(BASE_DIR, "intents.json")

DATA_DIR = os.path.join(BASE_DIR, "data")
FEEDBACK_FILE = os.path.join(DATA_DIR, "feedback.json")
CONFUSION_FILE = os.path.join(DATA_DIR, "confusion.json")

os.makedirs(DATA_DIR, exist_ok=True)

# ----------------------------
# Load intents JSON
# ----------------------------
try:
    with open(INTENTS_FILE, "r", encoding="utf-8") as f:
        intents = json.load(f)
except FileNotFoundError:
    print(f"Error: '{INTENTS_FILE}' not found.")
    intents = {"intents": []}

# ----------------------------
# Helper functions
# ----------------------------
def preprocess(sentence):
    tokens = re.findall(r'\b\w+\b', sentence.lower())
    return tokens

def predict_intent(message):
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

# ----------------------------
# Reinforcement Learning Helpers
# ----------------------------
def load_feedback():
    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_feedback(data):
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def update_feedback(tag, response, reward=1):
    feedback = load_feedback()
    key = f"{tag}|{response}"
    feedback[key] = feedback.get(key, 0) + reward
    save_feedback(feedback)

# ----------------------------
# Confusion Matrix Helpers
# ----------------------------
def load_confusion():
    try:
        with open(CONFUSION_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_confusion(matrix):
    with open(CONFUSION_FILE, "w", encoding="utf-8") as f:
        json.dump(matrix, f, indent=4)

def update_confusion(actual_tag, predicted_tag):
    """
    Updates confusion matrix with actual vs predicted intent.
    """
    matrix = load_confusion()
    if actual_tag not in matrix:
        matrix[actual_tag] = {}
    matrix[actual_tag][predicted_tag] = matrix[actual_tag].get(predicted_tag, 0) + 1
    save_confusion(matrix)

# ----------------------------
# Response Selection (RTC + Self-Learning)
# ----------------------------
def get_response(message, actual_intent=None):
    """
    Returns a response for the message.
    Uses reinforcement ranking to select the best response,
    and updates feedback automatically for self-learning.
    Optionally logs confusion matrix if actual_intent is provided.
    """
    tag = predict_intent(message)
    feedback = load_feedback()

    # Update confusion matrix if actual intent is known
    if actual_intent:
        update_confusion(actual_intent, tag)

    for intent in intents.get('intents', []):
        if intent.get('tag') == tag:
            responses = intent.get('responses', [])

            if not responses:
                break

            # Rank responses using feedback scores
            scored_responses = []
            for r in responses:
                key = f"{tag}|{r}"
                score = feedback.get(key, 0)
                scored_responses.append((r, score))

            # Sort responses by score (descending)
            scored_responses.sort(key=lambda x: x[1], reverse=True)

            # Pick the top-scored responses
            best_score = scored_responses[0][1]
            best_candidates = [r for r, s in scored_responses if s == best_score]

            # Randomly select one from top candidates
            chosen_response = random.choice(best_candidates)

            # Self-learning: Update feedback
            update_feedback(tag, chosen_response, reward=1)

            return chosen_response

    # Fallback response
    return "Sorry, I don't understand yet, but I can connect you to support."
