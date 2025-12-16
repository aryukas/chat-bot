from flask import Flask, request, jsonify, render_template
from chatbot import get_response, load_feedback
from flask_cors import CORS  # optional

app = Flask(__name__)
CORS(app)  # allow cross-origin requests

# ----------------------------
# Routes
# ----------------------------
@app.route('/')
def home():
    """
    Serve the main HTML page index.html.
    Make sure index.html is in the 'templates' folder.
    """
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to get chatbot responses.
    Expects JSON: {"message": "user message"}
    Returns JSON: {"reply": "bot response"}
    """
    try:
        user_msg = request.json.get('message', '')
        if not user_msg.strip():
            return jsonify({"reply": "Please type something!"})

        # Get response (self-learning happens inside get_response)
        reply = get_response(user_msg)

        return jsonify({"reply": reply})

    except Exception as e:
        print("Error in /chat:", e)
        return jsonify({"reply": "Sorry, there was an error connecting to the server."})

# ----------------------------
# Optional route to check feedback
# ----------------------------
@app.route('/feedback', methods=['GET'])
def feedback():
    """
    Returns current feedback scores from feedback.json
    Useful for debugging/self-learning verification.
    """
    try:
        feedback_data = load_feedback()
        return jsonify(feedback_data)
    except Exception as e:
        print("Error loading feedback:", e)
        return jsonify({"error": "Cannot load feedback."})


# ----------------------------
# Run Flask server
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
