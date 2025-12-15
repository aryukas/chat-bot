from chatbot import get_response, load_feedback
messages = ["Hi", "Hi", "Hello", "Hi there"]
for msg in messages:
    reply = get_response(msg)
    print(f"User: {msg} -> Bot: {reply}")

print("\nCurrent Feedback:", load_feedback())
