from flask import Flask, request, jsonify, render_template
from chatbot import get_response
from flask_cors import CORS  # optional 

app = Flask(__name__)
CORS(app)  # allow cross-origin requests 

# ----------------------------
# Routes
# ----------------------------
@app.route('/')
def home():
    """
    Serve the main HTML page.
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
        
        reply = get_response(user_msg)
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error in /chat:", e)
        return jsonify({"reply": "Sorry, there was an error connecting to the server."})

# ----------------------------
# Run Flask server
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
