from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os

# Initialize Flask app
app = Flask(__name__, template_folder='template')
CORS(app)

# Load predefined responses from JSON
with open(os.path.join(os.path.dirname(__file__), 'cusbot.json'), 'r', encoding='utf-8') as file:
    responses = json.load(file)

@app.route('/')
def index():
    return render_template('cusbotwrk.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').strip().lower()

    # Check predefined responses from the JSON file
    bot_response = responses.get(user_message, responses.get("default"))

    return jsonify({"message": bot_response}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
