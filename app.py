from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Serve HTML file
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Admission Bot Knowledge Base
responses = {
    "hello": "Hello! Welcome to University Admission Bot. How can I help you?",
    "hi": "Hi! Ask me anything about admissions.",
    "admission": "Admission process starts in June and ends in August.",
    "fees": "Average yearly fees is around ₹50,000 depending on course.",
    "documents": "You need 10th marksheet, 12th marksheet, ID proof, passport photo.",
    "courses": "We offer BCA, BBA, BSc IT, Engineering and Management courses.",
    "scholarship": "Scholarships available based on merit and category.",
    "contact": "You can contact admission office at 9876543210."
}

def get_bot_response(message):
    message = message.lower()

    for key in responses:
        if key in message:
            return responses[key]

    return "Please ask about admission, fees, courses, or documents."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    bot_reply = get_bot_response(user_message)

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)


