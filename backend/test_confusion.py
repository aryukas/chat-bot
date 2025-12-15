from chatbot import get_response, load_confusion

# Sample test dataset: message -> actual intent
test_data = {
    "Hi": "greeting",
    "Hello there": "greeting",
    "What is TMS?": "tms_definition",
    "Explain transport management system": "tms_definition",
    "Bye": "goodbye"
}

# Run the test
for msg, actual_intent in test_data.items():
    reply = get_response(msg, actual_intent=actual_intent)
    print(f"User: {msg} | Bot: {reply}")

# Check the confusion matrix
conf_matrix = load_confusion()
print("\nCurrent Confusion Matrix:")
for actual, preds in conf_matrix.items():
    print(f"{actual}: {preds}")
